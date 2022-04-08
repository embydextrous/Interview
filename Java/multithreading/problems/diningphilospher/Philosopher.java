package multithreading.problems.diningphilospher;

import multithreading.problems.diningphilospher.Chopstick.State;

public class Philosopher implements Runnable {
    private int id;
    private volatile boolean full;
    private Chopstick lefChopstick;
    private Chopstick righChopstick;
    private int eatingCounter;

    public Philosopher(int id, Chopstick lefChopstick, Chopstick righChopstick) {
        this.id = id;
        this.lefChopstick = lefChopstick;
        this.righChopstick = righChopstick;
    }

    @Override
    public void run() {
        while (!full) {
            think();
            boolean leftChopstickPicked = false;
            boolean rightChopStickPicked = false;

            try {
                leftChopstickPicked = lefChopstick.pickUp(this, State.LEFT);
                rightChopStickPicked = righChopstick.pickUp(this, State.RIGHT);
                if (leftChopstickPicked && rightChopStickPicked) {
                    eat();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                if (leftChopstickPicked) {
                    lefChopstick.putDown(this, State.LEFT);
                }
                if (rightChopStickPicked) {
                    righChopstick.putDown(this, State.RIGHT);
                }
            }
        }
    }

    private void think() {
        System.out.println(this + " is thinking...");
        try {
            Thread.sleep(250);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void eat() throws InterruptedException {
        System.out.println(this + " is eating...");
        eatingCounter++;
        Thread.sleep(40);
    }

    public void setFull(boolean full) {
        this.full = full;
    }

    public boolean isFull() {
        return full;
    }

    public int eatingCounter() {
        return this.eatingCounter;
    }

    @Override
    public String toString() {
        return "Philosopher" + id;
    }
}
