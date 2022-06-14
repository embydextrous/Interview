package snakeladder;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.print("Enter number of players: ");
        Scanner sc = new Scanner(System.in);
        int numPlayers = sc.nextInt();
        Queue<Player> players = new LinkedList<>();
        for (int i = 0; i < numPlayers; i++) {
            System.out.println("Enter Player " + (i + 1) + " name: ");
            String name = sc.next();
            players.add(new Player(name));
        }
        System.out.print("Enter board size: ");
        int size = sc.nextInt();
        System.out.print("Enter number of snakes: ");
        int numSnakes = sc.nextInt();
        List<Snake> snakes = new ArrayList<>();
        for (int i = 0; i < numSnakes; i++) {
            System.out.println("Enter Snake " + (i + 1) + " head and tail: ");
            int head = sc.nextInt();
            int tail = sc.nextInt();
            snakes.add(new Snake(head, tail));
        }
        System.out.print("Enter number of ladders: ");
        int numLadders = sc.nextInt();
        List<Ladder> ladders = new ArrayList<>();
        for (int i = 0; i < numLadders; i++) {
            System.out.println("Enter Ladder " + (i + 1) + " start and end: ");
            int start = sc.nextInt();
            int end = sc.nextInt();
            ladders.add(new Ladder(start, end));
        }

        Board board = new Board(snakes, ladders, size);
        Dice dice = new Dice(6);
        Game game = new Game(players, board, dice);
        while (!game.isGameOver()) {
            game.makeMove();
        }
        for(Player player : game.getPlayersAtDestination()) {
            System.out.println(player.getName() + " finished " + player.getRank());
        }
    }
}
