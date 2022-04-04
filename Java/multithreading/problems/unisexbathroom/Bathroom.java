package multithreading.problems.unisexbathroom;

import java.util.Random;

/**
 * How to prevent starvation? We can use ReentrantLock with fairness.
 */
public class Bathroom {
    private BathroomUseState inUseBy = BathroomUseState.NONE;
    private final int maxUsers;
    private int currentUsers = 0;

    public Bathroom(int maxUsers) {
        this.maxUsers = maxUsers;
    }
    
    public void maleUseBathroom(String name) throws InterruptedException {
        synchronized(this) {
            while(inUseBy == BathroomUseState.WOMEN || currentUsers == maxUsers) {
                wait();
            }
            currentUsers++;
            inUseBy = BathroomUseState.MEN;
        }
        useBathroom(name);
        synchronized(this) {
            currentUsers--;
            if (currentUsers == 0) {
                inUseBy = BathroomUseState.NONE;
            }
            notifyAll();
        }
    }   

    public synchronized void femaleUseBathroom(String name) throws InterruptedException {
        synchronized(this) {
            while(inUseBy == BathroomUseState.MEN || currentUsers == maxUsers) {
                wait();
            }
            currentUsers++;
            inUseBy = BathroomUseState.WOMEN;
        }
        useBathroom(name);
        synchronized(this) {
            currentUsers--;
            if (currentUsers == 0) {
                inUseBy = BathroomUseState.NONE;
            }
            notifyAll();
        }
    }

    private void useBathroom(String name) throws InterruptedException {
        System.out.println(name + " ne mootna shuru kiya at " + System.currentTimeMillis() / 1000);
        Thread.sleep(1000 + new Random().nextInt(2000));
        System.out.println(name + " ne mootna khatam kiya at " + System.currentTimeMillis() / 1000);
    }

    enum BathroomUseState {
        MEN, WOMEN, NONE
    }
}
