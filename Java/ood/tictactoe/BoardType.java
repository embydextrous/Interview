package tictactoe;

enum BoardType {
    SMALL(3), MEDIUM(4), LARGE(5);

    private int size = 0;
    
    BoardType(int size) {
        this.size = size;
    }

    public int getSize() {
        return size;
    }
}
