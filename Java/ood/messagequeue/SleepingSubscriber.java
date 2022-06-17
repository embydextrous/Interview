package messagequeue;

import messagequeue.model.Message;

public class SleepingSubscriber implements ISubscriber {
    private final String id;
    private final long sleepTime;

    public SleepingSubscriber(String id, long sleepTime) {
        this.id = id;
        this.sleepTime = sleepTime;
    }
    
    @Override
    public String getId() {
        return id;
    }

    @Override
    public void consume(Message message) throws InterruptedException {
        System.out.println("Subscriber: " + id + " started consuming: " + message.getContent());
        Thread.sleep(sleepTime);
        System.out.println("Subscriber: " + id + " done consuming: " + message.getContent());
    }
}
