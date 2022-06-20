package bookmyshow.model;

import java.sql.Date;
import java.util.UUID;

public class Show {
    private final String id;
    private final Movie movie;
    private final Screen screen;
    private final Date startTime;
    private final int durationInSeconds;
    
    public Show(Movie movie, Screen screen, Date startTime, int durationInSeconds) {
        this.id = UUID.randomUUID().toString();
        this.movie = movie;
        this.screen = screen;
        this.startTime = startTime;
        this.durationInSeconds = durationInSeconds;
    }

    public String getId() {
        return id;
    }

    public Movie getMovie() {
        return movie;
    }

    public Screen getScreen() {
        return screen;
    }

    public Date getStartTime() {
        return startTime;
    }

    public int getDurationInSeconds() {
        return durationInSeconds;
    }
}
