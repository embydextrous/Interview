package messagequeue;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

import messagequeue.handlers.TopicHandler;
import messagequeue.model.Message;
import messagequeue.model.Topic;
import messagequeue.model.TopicSubscriber;

public class MessageQueue {
    private final Map<String, TopicHandler> topicHandlers;

    public MessageQueue() {
        this.topicHandlers = new HashMap<>();
    }

    public Topic createTopic(String topicName) {
        Topic topic = new Topic(topicName, UUID.randomUUID().toString());
        TopicHandler topicHandler = new TopicHandler(topic);
        topicHandlers.put(topic.getId(), topicHandler);
        System.out.println("Created topic: " + topic.getName());
        return topic;
    }

    public void subscribe(ISubscriber subscriber, Topic topic) {
        topic.addSubscriber(new TopicSubscriber(subscriber));
        System.out.println(subscriber.getId() + " subscribed to topic: " + topic.getName());
    }

    public void publish(Topic topic, Message message) {
        topic.addMessage(message);
        System.out.println(message.getContent() + " published to topic: " + topic.getName());
        new Thread(() -> topicHandlers.get(topic.getId()).publish()).start();;
    }

    public void resetOffset(Topic topic, ISubscriber subscriber, int offset) {
        for (TopicSubscriber topicSubscriber : topic.getSubscribers()) {
            if (topicSubscriber.getSubscriber().equals(subscriber)) {
                topicSubscriber.getOffset().set(offset);
                new Thread(() -> topicHandlers.get(topic.getId()).startWorker(topicSubscriber)).start();
                break;
            }
        }
    }
}
