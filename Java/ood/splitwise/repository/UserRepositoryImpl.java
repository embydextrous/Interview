package splitwise.repository;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import splitwise.exceptions.NoSuchUserException;
import splitwise.model.User;

public class UserRepositoryImpl implements UserRepository {
    private final Map<String, User> users;

    public UserRepositoryImpl() {
        users = new HashMap<>();
    }

    @Override
    public List<User> getAllUsers() {
        return users.values().stream().collect(Collectors.toList());
    }

    @Override
    public User getUser(String id) {
        if (!users.containsKey(id)) {
            throw new NoSuchUserException("User with id " + id + " does not exist.");
        }
        return users.get(id);
    }

    @Override
    public void addUser(User user) {
        users.put(user.getId(), user);
    }
}
