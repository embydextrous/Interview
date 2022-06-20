package bookmyshow.controllers;

import java.util.List;
import java.util.stream.Collectors;

import bookmyshow.model.Seat;
import bookmyshow.model.Show;
import bookmyshow.service.BookingService;
import bookmyshow.service.ShowService;
import bookmyshow.service.TheatreService;

public class BookingController {
    private final ShowService showService;
    private final BookingService bookingService;
    private final TheatreService theatreService;

    public BookingController(ShowService showService, BookingService bookingService, TheatreService theatreService) {
        this.showService = showService;
        this.bookingService = bookingService;
        this.theatreService = theatreService;
    }

    public String createBooking(String user, String showId, List<String> seatsIds) {
        final Show show = showService.getShow(showId);
        final List<Seat> seats = seatsIds.stream().map(theatreService::getSeat).collect(Collectors.toList());
        return bookingService.createBooking(user, show, seats).getId();
    }
}
