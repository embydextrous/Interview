package splitwise.exceptions;

public class NoSuchExpenseException extends RuntimeException {
    public NoSuchExpenseException(String message) {
        super(message);
    }
}
