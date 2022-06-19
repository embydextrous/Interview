package splitwise.model;

import java.util.UUID;

public class User {
    private String id;
    private String name;
    private String email;
    private String phoneNumber;
    private double balance;

    public User(String name, String email, String phoneNumber) {
        this.id = UUID.randomUUID().toString();
        this.name = name;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.balance = 0.0;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public double getBalance() {
        return balance;
    }

    public double updateAndGetBalance(double incrementBy) {
        balance = balance + incrementBy;
        return balance;
    }
}
