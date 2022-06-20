package bookmyshow.provider;

import java.util.List;

import bookmyshow.model.Seat;
import bookmyshow.model.Show;
import bookmyshow.model.User;

public interface SeatLockProvider {
    void lockSeats(Show show, List<Seat> seats, String user);
    void unlockSeats(Show show, List<Seat> seats, String user);
    boolean validateLock(Show show, Seat seat, String user);

    List<Seat> getLockedSeats(Show show);
}
