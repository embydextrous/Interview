package messagequeue;

import messagequeue.model.Message;

public interface ISubscriber {
    
    String getId();
    void consume(Message message) throws InterruptedException;
}
