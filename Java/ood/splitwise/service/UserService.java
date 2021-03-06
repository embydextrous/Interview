package splitwise.service;

import java.util.List;

import splitwise.model.User;
import splitwise.repository.UserRepository;

public class UserService {
    private UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User addUser(String name, String email, String phoneNumber){
        User user = new User(name, email, phoneNumber);
        userRepository.addUser(user);
        return user;
    }

    public User getUser(String id) {
        return userRepository.getUser(id);
    }

    public List<User> getAllUsers() {
        return userRepository.getAllUsers();
    }
}
