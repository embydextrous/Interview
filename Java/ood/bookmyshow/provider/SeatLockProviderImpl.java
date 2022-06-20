package bookmyshow.provider;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import bookmyshow.exceptions.SeatTemporarilyUnavailableException;
import bookmyshow.model.Seat;
import bookmyshow.model.SeatLock;
import bookmyshow.model.Show;

public class SeatLockProviderImpl implements SeatLockProvider {
    
    private final Integer lockTimeout;
    private final Map<Show, Map<Seat, SeatLock>> locks;
    
    public SeatLockProviderImpl(Integer lockTimeout) {
        this.lockTimeout = lockTimeout;
        this.locks = new HashMap<>();
    }

    @Override
    synchronized public void lockSeats(Show show, List<Seat> seats, String user) {
        for(Seat seat : seats) {
            if (isSeatLocked(show, seat)) {
                throw new SeatTemporarilyUnavailableException();
            }
        }

        for (Seat seat : seats) {
            lockSeat(show, seat, user);
        }
    }

    @Override
    public void unlockSeats(Show show, List<Seat> seats, String user) {
        for(Seat seat : seats) {
            if (validateLock(show, seat, user)) {
                unlockSeat(show, seat);
            }
        }
    }

    @Override
    public boolean validateLock(Show show, Seat seat, String user) {
        return isSeatLocked(show, seat) && locks.get(show).get(seat).getLockedBy().equals(user);
    }

    @Override
    public List<Seat> getLockedSeats(Show show) {
        if (!locks.containsKey(show)) {
            return new ArrayList<>();
        }
        final List<Seat> lockedSeats = new ArrayList<>();

        for (Seat seat : locks.get(show).keySet()) {
            if (isSeatLocked(show, seat)) {
                lockedSeats.add(seat);
            }
        }
        return lockedSeats;
    }

    private void unlockSeat(Show show, Seat seat) {
        if (!locks.containsKey(show)) {
            return;
        }
        locks.get(show).remove(seat);
    }

    private void lockSeat(Show show, Seat seat, String user) {
        if (!locks.containsKey(show)) {
            locks.put(show, new HashMap<>());
        }
        final SeatLock seatLock = new SeatLock(seat, show, lockTimeout, new Date(), user);
        locks.get(show).put(seat, seatLock);
    }

    private boolean isSeatLocked(Show show, Seat seat) {
        return locks.containsKey(show) && locks.get(show).containsKey(seat) && !locks.get(show).get(seat).isLockExpired();
    }
}
