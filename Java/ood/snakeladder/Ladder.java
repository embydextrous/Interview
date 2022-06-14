package snakeladder;

public class Ladder {
    private final int start;
    private final int end;
    
    public Ladder(int start, int end) {
        this.start = start;
        this.end = end;
    }

    public int getEnd() {
        return end;
    }

    public int getStart() {
        return start;
    }
}
