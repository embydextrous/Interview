package splitwise.service;

import java.util.Map;

import splitwise.model.Expense;
import splitwise.model.ExpenseMetaData;
import splitwise.model.ExpenseType;
import splitwise.model.User;
import splitwise.repository.ExpenseRepository;

public class ExpenseService {
    private ExpenseRepository expenseRepository;
    private Expense.ExpenseFactory expenseFactory;

    public ExpenseService(ExpenseRepository expenseRepository, Expense.ExpenseFactory expenseFactory) {
        this.expenseRepository = expenseRepository;
        this.expenseFactory = expenseFactory;
    }

    public Expense addExpense(double amount, User paidBy, ExpenseType expenseType, ExpenseMetaData expenseMetaData, Map<User, Double> breakup) {
        Expense expense = null;
        if (expenseType == ExpenseType.EQUAL) {
            expense = expenseFactory.createEqualExpense(amount, paidBy, expenseMetaData, breakup.keySet());
        }
        if (expenseType == ExpenseType.EXACT) {
            expense = expenseFactory.createExactExpense(amount, paidBy, expenseMetaData, breakup);
        }
        if (expenseType == ExpenseType.PERCENT) {
            expense = expenseFactory.createPercentExpense(amount, paidBy, expenseMetaData, breakup);
        }
        if (expense == null) {
            throw new IllegalArgumentException("Invalid Expense Type");
        }
        expenseRepository.addExpense(expense);
        return expense;
    }

    public Expense getExpense(String id) {
        return expenseRepository.getExpense(id);
    }

    public Expense settleExpense(String id) {
        Expense expense = expenseRepository.getExpense(id);
        expense.setSettled(true);
        return expense;
    }
}
