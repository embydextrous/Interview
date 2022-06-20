package bookmyshow.controllers;

import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

import bookmyshow.model.Movie;
import bookmyshow.model.Screen;
import bookmyshow.model.Seat;
import bookmyshow.model.Show;
import bookmyshow.service.MovieService;
import bookmyshow.service.SeatAvailabilityService;
import bookmyshow.service.ShowService;
import bookmyshow.service.TheatreService;

public class ShowController {
    private final SeatAvailabilityService seatAvailabilityService;
    private final ShowService showService;
    private final TheatreService theatreService;
    private final MovieService movieService;

    public ShowController(SeatAvailabilityService seatAvailabilityService, ShowService showService,
            TheatreService theatreService, MovieService movieService) {
        this.seatAvailabilityService = seatAvailabilityService;
        this.showService = showService;
        this.theatreService = theatreService;
        this.movieService = movieService;
    }

    public String createShow(String movieId, String screenId, Date startTime, Integer durationInSeconds) {
        final Screen screen = theatreService.getScreen(screenId);
        final Movie movie = movieService.getMovie(movieId);
        return showService.createShow(movie, screen, startTime, durationInSeconds).getId();
    }

    public List<String> getAvailableSeats(String showId) {
        final Show show = showService.getShow(showId);
        final List<Seat> availableSeats = seatAvailabilityService.getAvailableSeats(show);
        return availableSeats.stream().map(Seat::getId).collect(Collectors.toList());
    }
}
