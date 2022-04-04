package multithreading.problems.tokenbucket;

public class TokenBucketDemo {
    public static void main(String[] args) throws InterruptedException {
        TokenBucket tokenBucket = TokenBucketFactory.create(5, true);

        Thread.sleep(10000);

        for (int i = 0; i < 10; i++) {
            Thread t = new Thread(() -> {
                try {
                    tokenBucket.awaitToken();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
            t.setName("Thread" + i);
            t.start();
        }
        Thread.sleep(10000);
    }
}
