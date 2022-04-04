package multithreading.problems.tokenbucket;

public class SimpleTokenBucket implements TokenBucket {
    private final int MAX_TOKENS;
    private long lastTokenTime = System.currentTimeMillis();
    private int tokens;

    public SimpleTokenBucket(int maxtokens) {
        this.MAX_TOKENS = maxtokens;
    }

    @Override
    public synchronized void awaitToken() throws InterruptedException {
        tokens += (System.currentTimeMillis() - lastTokenTime) / TOKEN_ISSUE_RATE_MS;
        if (tokens > MAX_TOKENS) {
            tokens = MAX_TOKENS;
        }
        if (tokens == 0) {
            Thread.sleep(TOKEN_ISSUE_RATE_MS);
        } else {
            tokens--;
        }
        lastTokenTime = System.currentTimeMillis();
        System.out.println(
            "Granted token to " + Thread.currentThread().getName() + " at " + lastTokenTime);
    }
}
