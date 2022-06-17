package messagequeue.model;

import java.util.ArrayList;
import java.util.List;

public class Topic {
    private final String name;
    private final String id;
    private final List<Message> messages;
    private final List<TopicSubscriber> subscribers;
    
    public Topic(String name, String id) {
        this.name = name;
        this.id = id;
        this.messages = new ArrayList<>();
        this.subscribers = new ArrayList<>();
    }

    public synchronized void addMessage(Message message) {
        messages.add(message);
    }

    public void addSubscriber(TopicSubscriber subscriber) {
        subscribers.add(subscriber);
    }

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    public List<TopicSubscriber> getSubscribers() {
        return subscribers;
    }

    public List<Message> getMessages() {
        return messages;
    }
}
