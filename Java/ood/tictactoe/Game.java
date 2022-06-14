package tictactoe;

public class Game {
    private Board board;
    private Player player1;
    private Player player2;
    // 0 denotes player 1 turn and 1 denotes player 0 turn
    private int turn;
    private Result result;
    private int numberMoves;

    Game(BoardType type, Player player1, Player player2) {
        this.board = new Board.Factory().createBoard(type);
        this.player1 = player1;
        this.player2 = player2;
        this.turn = 0;
        this.numberMoves = 0;
        this.result = Result.UNDECIDED;
    }

    public Board getBoard() {
        return board;
    }

    public Result getResult() {
        return result;
    }

    public Player getPlayer1() {
        return player1;
    }

    public Player getPlayer2() {
        return player2;
    }

    public Player getCurrentPlayer() {
        return turn == 0 ? player1 : player2;
    }

    public void makeMove(int row, int col) {
        Player playedBy = turn == 0 ? player1 : player2;
        if (!isValidMove(row, col)) {
            System.out.println("Invalid Move. Please try again.");
        } else {
            board.getBoard()[row][col] = playedBy.getPiece();
            numberMoves++;
            checkAndStoreResult(playedBy, row, col);
            turn = Math.abs(turn - 1);
        }
    }

    public void printBoard() {
        for(int i = 0; i < board.getType().getSize(); i++) {
            for(int j = 0; j < board.getType().getSize(); j++) {
                String toPrint = board.getBoard()[i][j] == null ? "-" : board.getBoard()[i][j] + "";
                System.out.print(toPrint + " ");
            }
            System.out.println();
        }
    }

    private boolean isValidMove(int row, int col) {
        return row >= 0 && row < board.getType().getSize()
            && col >= 0 && col < board.getType().getSize()
            && board.getBoard()[row][col] == null;
    }

    private void checkAndStoreResult(Player playedby, int row, int col) {
        // check row
        boolean hasWon = true;
        for (int i = 0; i < board.getType().getSize(); i++) {
            if (board.getBoard()[row][i] == null || board.getBoard()[row][i] != playedby.getPiece()) {
                hasWon = false;
                break;
            }
        }
        if (hasWon) {
            result = turn == 0 ? Result.PLAYER1_WON : Result.PLAYER2_WON;
            return;
        }

        // check column
        hasWon = true;
        for (int i = 0; i < board.getType().getSize(); i++) {
            if (board.getBoard()[i][col] == null || board.getBoard()[i][col] != playedby.getPiece()) {
                hasWon = false;
                break;
            }
        }
        if (hasWon) {
            result = turn == 0 ? Result.PLAYER1_WON : Result.PLAYER2_WON;
            return;
        }

        // check main diagonal
        if (row == col) {
            hasWon = true;
            for (int i = 0; i < board.getType().getSize(); i++) {
                if (board.getBoard()[i][i] == null || board.getBoard()[i][i] != playedby.getPiece()) {
                    hasWon = false;
                    break;
                }
            }
            if (hasWon) {
                result = turn == 0 ? Result.PLAYER1_WON : Result.PLAYER2_WON;
                return;
            }
        }

        // check second diagonal
        if (row + col == board.getType().getSize() - 1) {
            hasWon = true;
            for (int i = 0; i < board.getType().getSize(); i++) {
                if (board.getBoard()[i][board.getType().getSize() - i - 1] == null || board.getBoard()[i][board.getType().getSize() - i - 1] != playedby.getPiece()) {
                    hasWon = false;
                    break;
                }
            }
            if (hasWon) {
                result = turn == 0 ? Result.PLAYER1_WON : Result.PLAYER2_WON;
                return;
            }
        }

        if (numberMoves == board.getType().getSize() * board.getType().getSize()) {
            result = Result.DRAW;
        }
    }

    public boolean isGameOver() {
        return result != Result.UNDECIDED;
    }
}
