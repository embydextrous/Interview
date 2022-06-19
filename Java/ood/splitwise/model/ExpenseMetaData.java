package splitwise.model;

public class ExpenseMetaData {
    private final String title;
    private final String description;

    public ExpenseMetaData(String title, String description) {
        this.title = title;
        this.description = description;
    }

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }
}