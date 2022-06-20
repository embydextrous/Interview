package bookmyshow.controllers;

import bookmyshow.model.Screen;
import bookmyshow.model.Theatre;
import bookmyshow.service.TheatreService;

public class TheatreController {
    private final TheatreService theatreService;
    
    public TheatreController(TheatreService theatreService) {
        this.theatreService = theatreService;
    }

    public TheatreService getTheatreService() {
        return theatreService;
    }

    public String createTheatre(final String theatreName) {
        return theatreService.createTheatre(theatreName).getId();
    }

    public String createScreenInTheatre(String screenName, String theatreId) {
        final Theatre theatre = theatreService.getTheatre(theatreId);
        return theatreService.createScreenInTheatre(screenName, theatre).getId();
    }

    public String createSeatInScreen(Integer rowNo, Integer seatNo, String screenId) {
        final Screen screen = theatreService.getScreen(screenId);
        return theatreService.createSeatInScreen(rowNo, seatNo, screen).getId();
    }
}
