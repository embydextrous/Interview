package splitwise.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import splitwise.model.ExpenseMetaData;
import splitwise.model.ExpenseType;
import splitwise.model.User;

public class Main {
    public static void main(String[] args) {
        SplitwiseApp app = SplitwiseApp.create();
        List<User> users = new ArrayList<>();
        User user = app.addUser("Arjit", "arjit.agarwal.1000@gmail.com", "9930560474");
        users.add(user);
        user = app.addUser("Sachi", "sachi@gmail.com", "8372736267");
        users.add(user);
        user = app.addUser("Arpit", "arpit@gmail.com", "9383834747");
        users.add(user);
        user = app.addUser("Addam", "addam@gmail.com", "9272387362");
        users.add(user);
        user = app.addUser("Atulya", "atulya@gmail.com", "9287232442");
        users.add(user);

        HashMap<User, Double> breakup = new HashMap<>();
        breakup.put(users.get(1), 0.0);
        breakup.put(users.get(2), 0.0);
        breakup.put(users.get(3), 0.0);
        app.addExpense(300, users.get(0), ExpenseType.EQUAL, new ExpenseMetaData("Dinner at Haat", ""), 
            breakup);
        app.getBalances().entrySet().forEach((entry) -> { 
            String name = entry.getKey().getName();
            double balance = entry.getValue();
            String output = null;
            if (balance > 0) {
                output = name + " has to collect Rs. " + balance;
            } else if (balance < 0) {
                output = name + " owes Rs. " + -1 * balance;
            } else {
                output = name + " is settled up";
            }
            System.out.println(output);
        });
    }
}
