package multithreading.problems.barrier;

public interface Barrier {
    public void await() throws InterruptedException;
}
