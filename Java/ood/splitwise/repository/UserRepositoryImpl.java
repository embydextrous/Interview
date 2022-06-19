package splitwise.repository;

import java.util.ArrayList;
import java.util.List;

import splitwise.model.User;

public class UserRepositoryImpl implements UserRepository {
    private final List<User> users;

    public UserRepositoryImpl() {
        users = new ArrayList<>();
    }

    @Override
    public List<User> getAllUsers() {
        return users;
    }

    @Override
    public User getUser(String id) {
        return users.stream().filter(user -> user.getId() == id).findFirst().orElse(null);
    }

    @Override
    public void addUser(User user) {
        users.add(user);
    }
}
