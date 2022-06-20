package splitwise.repository;

import java.util.HashMap;
import java.util.Map;

import splitwise.exceptions.NoSuchExpenseException;
import splitwise.model.Expense;

public class ExpenseRepositoryImpl implements ExpenseRepository {
    
    private final Map<String, Expense> expenses;

    public ExpenseRepositoryImpl() {
        this.expenses = new HashMap<>();
    }

    @Override
    public void addExpense(Expense expense) {
        this.expenses.put(expense.getId(), expense);
    }

    @Override
    public Expense getExpense(String id) {
        if (!expenses.containsKey(id)) {
            throw new NoSuchExpenseException("Expense with id " + id + " does not exist.");
        }
        return expenses.get(id);
    }
}
