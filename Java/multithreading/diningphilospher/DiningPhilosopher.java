package multithreading.diningphilospher;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class DiningPhilosopher {
    public static void main(String[] args) throws InterruptedException {
        ExecutorService executor = Executors.newFixedThreadPool(Constants.NUM_PHILOSOPHERS);
        Philosopher[] philosophers = new Philosopher[Constants.NUM_PHILOSOPHERS];
        Chopstick[] chopSticks = new Chopstick[Constants.NUM_CHOPSTICKS];
        for (int i = 0; i < Constants.NUM_CHOPSTICKS; i++) {
            chopSticks[i] = new Chopstick(i + 1);
        }
        for (int i = 0; i < Constants.NUM_PHILOSOPHERS; i++) {
            Chopstick leftChopstick = chopSticks[i];
            Chopstick righChopstick = chopSticks[(i + 1) % Constants.NUM_CHOPSTICKS];
            philosophers[i] = new Philosopher(i + 1, leftChopstick, righChopstick);
        }

        try {
            for (int i = 0; i < Constants.NUM_PHILOSOPHERS; i++) {
                executor.submit(philosophers[i]);
            }
            executor.awaitTermination(Constants.SIMULATION_RUNNING_TIME, TimeUnit.MILLISECONDS);
            for (Philosopher philosopher : philosophers) {
                philosopher.setFull(true);
            }
            
        } finally {
            executor.shutdown();
            while (!executor.isTerminated()) {
                Thread.sleep(1000);
            }
            for (Philosopher philosopher : philosophers) {
                System.out.println(philosopher + " eat " + philosopher.eatingCounter() + " times.");
            }
        }
    }
}
