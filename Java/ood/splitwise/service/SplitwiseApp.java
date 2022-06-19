package splitwise.service;

import java.util.Map;
import java.util.stream.Collectors;

import splitwise.exceptions.NoSuchExpenseException;
import splitwise.exceptions.NoSuchUserException;
import splitwise.model.Expense;
import splitwise.model.ExpenseMetaData;
import splitwise.model.ExpenseType;
import splitwise.model.User;
import splitwise.model.Expense.ExpenseFactory;
import splitwise.repository.ExpenseRepository;
import splitwise.repository.ExpenseRepositoryImpl;
import splitwise.repository.UserRepository;
import splitwise.repository.UserRepositoryImpl;

public class SplitwiseApp {
    private ExpenseService expenseService;
    private UserService userService;

    public SplitwiseApp(ExpenseService expenseService, UserService userService) {
        this.expenseService = expenseService;
        this.userService = userService;
    }

    public Map<User, Double> getBalances() {
        return userService.getAllUsers().stream().collect(Collectors.toMap(user -> user, user -> user.getBalance()));
    }

    public Double getBalance(String userId) {
        try {
            return userService.getUser(userId).getBalance();
        } catch(NoSuchUserException e) {
            System.out.println(e.getMessage());
            return null;
        }
    }

    public void settleExpense(String expenseId) {
        try {
            Expense expense = expenseService.settleExpense(expenseId);
            expense.getPaidBy().updateAndGetBalance(-1 * expense.getAmount());
            expense.getSplits().forEach(split -> split.getUser().updateAndGetBalance(split.getAmount()));
        } catch (NoSuchExpenseException e) {
            System.out.println(e.getMessage());
        }
    }

    public void addExpense(double amount, User paidBy, ExpenseType expenseType, ExpenseMetaData expenseMetaData, Map<User, Double> breakup) {
        Expense expense = expenseService.addExpense(amount, paidBy, expenseType, expenseMetaData, breakup);
        paidBy.updateAndGetBalance(amount);
        expense.getSplits().forEach(split -> split.getUser().updateAndGetBalance(-1 * split.getAmount()));
    }

    public User addUser(String name, String email, String phonenumber) {
        return userService.addUser(name, email, phonenumber);
    }

    public static SplitwiseApp create() {
        ExpenseFactory expenseFactory = new ExpenseFactory();
        ExpenseRepository expenseRepository = new ExpenseRepositoryImpl();
        ExpenseService expenseService = new ExpenseService(expenseRepository, expenseFactory);
        UserRepository userRepository = new UserRepositoryImpl();
        UserService userService = new UserService(userRepository);
        return new SplitwiseApp(expenseService, userService);
    }

}
