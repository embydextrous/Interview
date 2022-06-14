package tictactoe;

public class Board {
    private String title;
    private BoardType type;
    private Character[][] board;

    public Character[][] getBoard() {
        return board;
    }

    public String getTitle() {
        return title;
    }

    public BoardType getType() {
        return type;
    }


    private Board(String title, BoardType type, Character[][] board) {
        this.title = title;
        this.type = type;
        this.board = board;
    }

    static class Factory {
        public Board createBoard(BoardType type) {
            switch(type) {
                case SMALL : return new Board("3x3", type, new Character[3][3]);
                case MEDIUM : return new Board("4x4", type, new Character[4][4]);
                case LARGE : return new Board("5x5", type, new Character[5][5]);
                default : return new Board("3x3", type, new Character[3][3]);
            }
        }
    }
}
