package bookmyshow.model;

import java.util.UUID;

public class Movie {
    private final String id;
    private final String name;
    
    public Movie(String name) {
        this.id = UUID.randomUUID().toString();
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}
