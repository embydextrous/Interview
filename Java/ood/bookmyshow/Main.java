package bookmyshow;

import bookmyshow.controllers.BookingController;
import bookmyshow.controllers.MovieController;
import bookmyshow.controllers.PaymentsController;
import bookmyshow.controllers.ShowController;
import bookmyshow.controllers.TheatreController;
import bookmyshow.provider.SeatLockProvider;
import bookmyshow.provider.SeatLockProviderImpl;
import bookmyshow.repository.MovieRepositoryImpl;
import bookmyshow.service.BookingService;
import bookmyshow.service.MovieService;
import bookmyshow.service.PaymentService;
import bookmyshow.service.SeatAvailabilityService;
import bookmyshow.service.ShowService;
import bookmyshow.service.TheatreService;

public class Main {
    protected static BookingController bookingController;
    protected static ShowController showController;
    protected static TheatreController theatreController;
    protected static MovieController movieController;
    protected static PaymentsController paymentsController;

    public static void main(String[] args) {
        setupControllers(10, 2);
    }

    private static void setupControllers(int lockTimeout, int allowedRetries) {
        final SeatLockProvider seatLockProvider = new SeatLockProviderImpl(lockTimeout);
        final BookingService bookingService = new BookingService(seatLockProvider);
        final MovieService movieService = new MovieService(new MovieRepositoryImpl());
        final ShowService showService = new ShowService();
        final TheatreService theatreService = new TheatreService();
        final SeatAvailabilityService seatAvailabilityService
                = new SeatAvailabilityService(bookingService, seatLockProvider);
        final PaymentService paymentsService = new PaymentService(allowedRetries, seatLockProvider);

        bookingController = new BookingController(showService, bookingService, theatreService);
        showController = new ShowController(seatAvailabilityService, showService, theatreService, movieService);
        theatreController = new TheatreController(theatreService);
        movieController = new MovieController(movieService);
        paymentsController = new PaymentsController(paymentsService, bookingService);
        // create theatre
        // create movies
        // create screen
        // create seats
        // create show

        // Don't Implement All Services - Create Dummy Data
        // Focus on BookingService, PaymentService and SeatAvailabilityService
    }
}
