package splitwise.repository;

import java.util.List;

import splitwise.model.User;

public interface UserRepository {
    
    List<User> getAllUsers();
    void addUser(User user);
    User getUser(String id);
}
