package snakeladder;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/*
 * Other improvements - upto three die rolls
 * Send to Home
 */
public class Game {

    private Queue<Player> players = new LinkedList<>();
    private Board board;
    private Dice dice;
    private int nextRank = 1;
    private List<Player> playersAtDestination = new ArrayList<>();

    public List<Player> getPlayersAtDestination() {
        return playersAtDestination;
    }

    public Game(Queue<Player> players, Board board, Dice dice) {
        this.players = players;
        this.board = board;
        this.dice = dice;
    }

    public void makeMove() {
        Player player = players.poll();
        int diceValue = dice.roll();
        System.out.println(player.getName() + " rolled " + diceValue);
        if (player.getPosition() + diceValue == board.getDestination()) {
            assignAndIncrementRank(player);
            System.out.println(player.getName() + " reached destination. his rank is " + player.getRank());
            if (players.size() == 1) {
                System.out.println("Game Over!");
                assignAndIncrementRank(players.poll());
            }
        } else if (player.getPosition() + diceValue < board.getDestination()) {
            int newPosition = player.getPosition() + diceValue;
            Snake snake = board.getSnakeAtPosition(newPosition);
            Ladder ladder = board.getLadderAtPosition(newPosition);
            if (snake != null) {
                System.out.println(player.getName() + " bitten by snake at " + newPosition);
                newPosition = snake.getTail();
            } else if (ladder != null) {
                System.out.println(player.getName() + " took ladder at " + newPosition);
                newPosition = ladder.getEnd();
            }
            System.out.println(player.getName() + " moved to position " + newPosition);
            player.setPosition(newPosition);
            players.add(player);
        } else {
            players.add(player);
        }
    }

    public boolean isGameOver() {
        return players.size() == 0;
    }

    private void assignAndIncrementRank(Player player) {
        player.setRank(nextRank);
        playersAtDestination.add(player);
        nextRank++;
    } 
}
