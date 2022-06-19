package splitwise.repository;

import java.util.List;

import splitwise.model.Expense;

public interface ExpenseRepository {
    
    void addExpense(Expense expense);
    Expense getExpense(String id);
}
