package bookmyshow.model;

import java.util.List;
import java.util.UUID;

public class Booking {
    private final String id;
    private final Show show;
    private final List<Seat> seatsBooked;
    private final String user;
    private BookingStatus bookingStatus;
    
    public Booking(Show show, List<Seat> seatsBooked, String user) {
        this.id = UUID.randomUUID().toString();
        this.show = show;
        this.seatsBooked = seatsBooked;
        this.user = user;
        this.bookingStatus = BookingStatus.CREATED;
    }

    public String getId() {
        return id;
    }

    public Show getShow() {
        return show;
    }

    public List<Seat> getSeatsBooked() {
        return seatsBooked;
    }

    public String getUser() {
        return user;
    }

    public BookingStatus getBookingStatus() {
        return bookingStatus;
    }

    public boolean isConfirmed() {
        return bookingStatus == BookingStatus.CONFIRMED;
    }

    public void confirm() {
        if (this.bookingStatus != BookingStatus.CREATED) {
            throw new IllegalStateException();
        }
        this.bookingStatus = BookingStatus.CONFIRMED;
    }

    public void expire() {
        if (this.bookingStatus != BookingStatus.CREATED) {
            throw new IllegalStateException();
        }
        this.bookingStatus = BookingStatus.EXPIRED;
    }
}
