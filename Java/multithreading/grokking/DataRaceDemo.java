package multithreading.grokking;

public class DataRaceDemo {
    public static void main(String[] args) {
        SharedClass sharedObject = new SharedClass();
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    sharedObject.increment();
                }
            }
        }).start();
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    sharedObject.checkForDataRace();
                }
            }
        }).start();
    }
}

class SharedClass {
    private volatile int x = 0;
    private volatile int y = 0;

    public void increment() {
        x++;
        y++;
    }

    public void checkForDataRace() {
        if (y > x) {
            System.out.println("DataRace occured: " + " x: " + x + " y: " + y);
            throw new RuntimeException();
        }
    }
}