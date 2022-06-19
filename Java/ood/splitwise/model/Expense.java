package splitwise.model;

import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import java.util.stream.Collectors;

import splitwise.exceptions.InvalidExpenseException;

public class Expense {
    private final String id;
    private double amount;
    private User paidBy;
    private List<Split> splits;
    private ExpenseMetaData expenseMetaData;
    private ExpenseType expenseType;
    private boolean settled;

    private Expense(double amount, User paidBy, ExpenseMetaData expenseMetaData, ExpenseType expenseType,
            List<Split> splits) {
        this.id = UUID.randomUUID().toString();
        this.amount = amount;
        this.paidBy = paidBy;
        this.expenseMetaData = expenseMetaData;
        this.expenseType = expenseType;
        this.splits = splits;
        this.settled = false;
    }

    public double getAmount() {
        return amount;
    }

    public String getId() {
        return id;
    }

    public User getPaidBy() {
        return paidBy;
    }

    public ExpenseMetaData getExpenseMetaData() {
        return expenseMetaData;
    }

    public ExpenseType getExpenseType() {
        return expenseType;
    }

    public List<Split> getSplits() {
        return splits;
    }

    public boolean isSettled() {
        return settled;
    }

    public void setSettled(boolean settled) {
        this.settled = settled;
    }

    public static class ExpenseFactory {

        public Expense createExactExpense(
                double amount, User paidBy,
                ExpenseMetaData expenseMetaData,
                Map<User, Double> amountMap) {
            List<Split> splits = amountMap.entrySet().stream().map(entry -> new Split(entry.getKey(), entry.getValue()))
                    .collect(Collectors.toList());
            validateAndAddIfNeeded(amount, splits, paidBy);
            return new Expense(amount, paidBy, expenseMetaData, ExpenseType.EXACT, splits);
        }

        public Expense createEqualExpense(
                double amount, User paidBy,
                ExpenseMetaData expenseMetaData,
                Set<User> users) {
            double amountPerUser = amount / (users.size() + 1);
            List<Split> splits = users.stream().map(user -> new Split(user, amountPerUser)).collect(Collectors.toList());
            splits.add(new Split(paidBy, amountPerUser));
            validateAndAddIfNeeded(amount, splits, paidBy);
            return new Expense(amount, paidBy, expenseMetaData, ExpenseType.EQUAL, splits);
        }

        public Expense createPercentExpense(
            double amount, User paidBy,
            ExpenseMetaData expenseMetaData,
            Map<User, Double> percentMap
        ) {
            List<Split> splits = percentMap.entrySet().stream().map(entry -> new Split(entry.getKey(), (amount * entry.getValue()) / 100)).collect(Collectors.toList());
            validateAndAddIfNeeded(amount, splits, paidBy);
            return new Expense(amount, paidBy, expenseMetaData, ExpenseType.EQUAL, splits);
        }

        private void validateAndAddIfNeeded(double amount, List<Split> splits, User user) {
            double remainingAmount = amount - splits.stream().map(split -> split.getAmount()).reduce(0.0, (t, e) -> t + e);
            if (remainingAmount < 0) {
                throw new InvalidExpenseException("Split amount " + (amount + remainingAmount) + " exceeds total amount " + amount);
            }
            if (remainingAmount > 0) {
                splits.add(new Split(user, remainingAmount));
            }
        }
    }
}
