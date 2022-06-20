package bookmyshow.service;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import bookmyshow.exceptions.NotFoundException;
import bookmyshow.exceptions.ScreenAlreadyOccupiedException;
import bookmyshow.model.Movie;
import bookmyshow.model.Screen;
import bookmyshow.model.Show;

public class ShowService {
    private final Map<String, Show> shows;

    public ShowService() {
        this.shows = new HashMap<>();
    }

    public Show getShow(final String showId) {
        if (!shows.containsKey(showId)) {
            throw new NotFoundException();
        }
        return shows.get(showId);
    }

    public Show createShow(Movie movie, Screen screen, Date startTime, Integer durationInSeconds) {
        if (!checkIfShowCreationAllowed(screen, startTime, durationInSeconds)) {
            throw new ScreenAlreadyOccupiedException();
        }
        final Show show = new Show(movie, screen, startTime, durationInSeconds);
        this.shows.put(show.getId(), show);
        return show;
    }

    private boolean checkIfShowCreationAllowed(final Screen screen, final Date startTime, final Integer durationInSeconds) {
        return true;
    }
}
