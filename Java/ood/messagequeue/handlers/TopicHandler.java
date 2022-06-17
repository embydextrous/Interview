package messagequeue.handlers;

import java.util.HashMap;
import java.util.Map;

import messagequeue.model.Topic;
import messagequeue.model.TopicSubscriber;

public class TopicHandler {
    private final Topic topic;
    private final Map<String, SubscriberWorker> workers;

    public TopicHandler(Topic topic) {
        this.topic = topic;
        this.workers = new HashMap<>();
    }

    public void publish() {
        for (TopicSubscriber topicSubscriber : topic.getSubscribers()) {
            startWorker(topicSubscriber);
        }
    }

    public void startWorker(TopicSubscriber topicSubscriber) {
        String subscriberId = topicSubscriber.getSubscriber().getId();
        if (!workers.containsKey(subscriberId)) {
            SubscriberWorker subscriberWorker = new SubscriberWorker(topic, topicSubscriber);
            workers.put(subscriberId, subscriberWorker);
            new Thread(subscriberWorker).start();
        }
        SubscriberWorker subscriberWorker = workers.get(subscriberId);
        subscriberWorker.wakeUpIfNeeded();
    }
}
