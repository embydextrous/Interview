package bookmyshow.model;

import java.util.UUID;

public class Seat {
    private final String id;
    private final int rowNo;
    private final int seatno;
    
    public Seat(int rowNo, int seatno) {
        this.id = UUID.randomUUID().toString();
        this.rowNo = rowNo;
        this.seatno = seatno;
    }

    public int getRowNo() {
        return rowNo;
    }

    public int getSeatno() {
        return seatno;
    }

    public String getId() {
        return id;
    }
}
