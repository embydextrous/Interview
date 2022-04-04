package multithreading.problems.tokenbucket;

public class TokenBucketFactory {

    public static TokenBucket create(int maxTokens, boolean tokenDaemon) {
        if (tokenDaemon) {
            BackgroundThreadTokenBucket tokenBucket = new BackgroundThreadTokenBucket(maxTokens);
            tokenBucket.init();
            return tokenBucket;
        } else {
            return new SimpleTokenBucket(maxTokens);
        }
    }
}
