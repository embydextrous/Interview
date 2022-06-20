package bookmyshow.model;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class Theatre {
    private final String id;
    private final String name;
    private final List<Screen> screens;
    // Other data like address
    
    public Theatre(String name) {
        this.id = UUID.randomUUID().toString();
        this.name = name;
        this.screens = new ArrayList<>();
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public List<Screen> getScreens() {
        return screens;
    }

    public void addScreen(Screen screen) {
        this.screens.add(screen);
    }
}
