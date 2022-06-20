package bookmyshow.controllers;

import bookmyshow.service.BookingService;
import bookmyshow.service.PaymentService;

public class PaymentsController {
    private final PaymentService paymentService;
    private final BookingService bookingService;

    public PaymentsController(PaymentService paymentsService, BookingService bookingService) {
        this.paymentService = paymentsService;
        this.bookingService = bookingService;
    }

    public void paymentFailed(String bookingId, String user) {
        paymentService.processPaymentFailed(bookingService.getBooking(bookingId), user);
    }

    public void paymentSuccess(String bookingId, String user) {
        bookingService.confirmBooking(bookingService.getBooking(bookingId), user);
    }
}
