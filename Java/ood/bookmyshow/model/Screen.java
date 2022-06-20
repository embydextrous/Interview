package bookmyshow.model;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class Screen {
    private final String id;
    private final String name;
    private final Theatre theatre;
    private final List<Seat> seats;
   
    public Screen(String name, Theatre theatre) {
        this.id = UUID.randomUUID().toString();
        this.name = name;
        this.theatre = theatre;
        this.seats = new ArrayList<>();
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Theatre getTheatre() {
        return theatre;
    }

    public List<Seat> getSeats() {
        return seats;
    }

    public void addSeat(Seat seat) {
        this.seats.add(seat);
    }
}
