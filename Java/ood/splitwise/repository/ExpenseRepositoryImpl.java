package splitwise.repository;

import java.util.ArrayList;
import java.util.List;

import splitwise.model.Expense;

public class ExpenseRepositoryImpl implements ExpenseRepository {
    
    private final List<Expense> expenses;

    public ExpenseRepositoryImpl() {
        this.expenses = new ArrayList<>();
    }

    @Override
    public void addExpense(Expense expense) {
        
    }

    @Override
    public Expense getExpense(String id) {
        return expenses.stream().filter(expense -> expense.getId() == id).findFirst().orElse(null);
    }
}
