package messagequeue.handlers;

import messagequeue.model.Message;
import messagequeue.model.Topic;
import messagequeue.model.TopicSubscriber;

public class SubscriberWorker implements Runnable {
    private final Topic topic;
    private final TopicSubscriber topicSubscriber;
    
    public SubscriberWorker(Topic topic, TopicSubscriber topicSubscriber) {
        this.topic = topic;
        this.topicSubscriber = topicSubscriber;
    }

    @Override
    public void run() throws RuntimeException {
        synchronized (topicSubscriber) {
            while (true) {
                int currentOffset = topicSubscriber.getOffset().get();
                while (currentOffset >= topic.getMessages().size()) {
                    try {
                        topicSubscriber.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

                Message message = topic.getMessages().get(currentOffset);
                try {
                    topicSubscriber.getSubscriber().consume(message);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                topicSubscriber.getOffset().compareAndSet(currentOffset, currentOffset + 1);
            }
        }
    }

    synchronized public void wakeUpIfNeeded() {
        synchronized (topicSubscriber) {
            topicSubscriber.notify();
        }
    }
}
