package snakeladder;

import java.util.HashMap;
import java.util.List;

public class Board {
    private final HashMap<Integer, Snake> snakes = new HashMap<>();
    private final HashMap<Integer, Ladder> ladders = new HashMap<>();
    private final int size;
    private final int destination;
    
    public Board(List<Snake> snakes, List<Ladder> ladders, int size) {
        snakes.forEach(snake -> this.snakes.put(snake.getHead(), snake));
        ladders.forEach(ladder -> this.ladders.put(ladder.getStart(), ladder));        
        this.size = size;
        this.destination = size * size;
    } 

    public int getSize() {
        return size;
    }

    public Snake getSnakeAtPosition(int position) {
        if (snakes.containsKey(position)) {
            return snakes.get(position);
        }
        return null;
    }

    public Ladder getLadderAtPosition(int position) {
        if (ladders.containsKey(position)) {
            return ladders.get(position);
        }
        return null;
    }

    public int getDestination() {
        return destination;
    }
}
