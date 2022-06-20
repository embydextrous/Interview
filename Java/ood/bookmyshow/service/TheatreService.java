package bookmyshow.service;

import java.util.HashMap;
import java.util.Map;

import bookmyshow.exceptions.NotFoundException;
import bookmyshow.model.Screen;
import bookmyshow.model.Seat;
import bookmyshow.model.Theatre;

public class TheatreService {
    private final Map<String, Theatre> theatres;
    private final Map<String, Screen> screens;
    private final Map<String, Seat> seats;

    public TheatreService() {
        this.theatres = new HashMap<>();
        this.screens = new HashMap<>();
        this.seats = new HashMap<>();
    }

    public Seat getSeat(final String seatId) {
        if (!seats.containsKey(seatId)) {
            throw new NotFoundException();
        }
        return seats.get(seatId);
    }

    public Theatre getTheatre(final String theatreId) {
        if (!theatres.containsKey(theatreId)) {
            throw new NotFoundException();
        }
        return theatres.get(theatreId);
    }

    public Screen getScreen(final String screenId) {
        if (!screens.containsKey(screenId)) {
            throw new NotFoundException();
        }
        return screens.get(screenId);
    }

    public Theatre createTheatre(final String theatreName) {
        Theatre theatre = new Theatre(theatreName);
        theatres.put(theatre.getId(), theatre);
        return theatre;
    }

    public Screen createScreenInTheatre(final String screenName, final Theatre theatre) {
        Screen screen = createScreen(screenName, theatre);
        theatre.addScreen(screen);
        return screen;
    }

    public Seat createSeatInScreen(final Integer rowNo, final Integer seatNo, final Screen screen) {
        Seat seat = new Seat(rowNo, seatNo);
        seats.put(seat.getId(), seat);
        screen.addSeat(seat);

        return seat;
    }

    private Screen createScreen(final String screenName, final Theatre theatre) {
        Screen screen = new Screen(screenName, theatre);
        screens.put(screen.getId(), screen);
        return screen;
    }
}
