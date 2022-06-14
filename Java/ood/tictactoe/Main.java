package tictactoe;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter player 1 name: ");
        String name = sc.next();
        Player player1 = new Player(name, 'X');
        System.out.print("Enter player 2 name: ");
        name = sc.next();
        Player player2 = new Player(name, 'O');
        System.out.println("Choose board size:");
        System.out.println("Type 1 for 3x3");
        System.out.println("Type 2 for 4x4");
        System.out.println("Type 3 for 5x5");
        System.out.print("Enter: ");
        int c = sc.nextInt();
        BoardType type;
        if (c == 1) {
            type = BoardType.SMALL;
        } else if (c == 2) {
            type = BoardType.MEDIUM;
        } else if (c == 3) {
            type = BoardType.LARGE;
        } else {
            System.out.print("Invalid entry. Creating board of 3x3 size..");
            type = BoardType.SMALL;
        }
        
        Game game = new Game(type, player1, player2);
        while (game.getResult() == Result.UNDECIDED) {
            System.out.print(game.getCurrentPlayer().getName() + " enter your move:");
            int row = sc.nextInt();
            int col = sc.nextInt();
            game.makeMove(row, col);
            game.printBoard();
        }
        if (game.getResult() == Result.PLAYER1_WON) {
            System.out.println(game.getPlayer1().getName() + " Won!");
        } else if (game.getResult() == Result.PLAYER2_WON) {
            System.out.println(game.getPlayer2().getName() + " Won!");
        } else {
            System.out.println("Drawn!");
        }
    }
}
