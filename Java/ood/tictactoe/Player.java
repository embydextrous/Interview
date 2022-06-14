package tictactoe;

public class Player {
    private String name;
    private char piece;

    Player(String name, char piece) {
        this.name = name;
        this.piece = piece;
    }

    public String getName() {
        return name;
    }

    public char getPiece() {
        return piece;
    }
}
