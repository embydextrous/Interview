package snakeladder;

public class Player {
    private final String name;
    private int position;
    private int rank;

    public String getName() {
        return name;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public Player(String name) {
        this.name = name;
        this.position = 0;
        this.rank = 0;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }

    public int getRank() {
        return rank;
    }
}
