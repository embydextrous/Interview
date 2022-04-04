package multithreading.problems.tokenbucket;

public interface TokenBucket {
    public static final long TOKEN_ISSUE_RATE_MS = 1000;
    
    public void awaitToken() throws InterruptedException;
}
