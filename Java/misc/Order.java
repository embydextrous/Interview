package misc;

/**
 * Static Parent
 * Static Child
 * Inline Parent
 * Parent Constructor
 * Inline Child
 * Child Primary Constructor
 * Child Secondary Constructor
 */

public class Order {
    public static void main(String[] args) {
        new Children(4);
    }
}

class Parent {
    {
        System.out.println("Parent Init 1");
    }

    static {
        System.out.println("Parent Static 1");
    }

    Parent() {
        System.out.println("Parent Primary Constructor");
    }

    {
        System.out.println("Parent Init 2");
    }

    static {
        System.out.println("Parent Static 2");
    }
}

class Children extends Parent {
    private int a = 2;

    {
        System.out.println("Child Init 1");
        System.out.println(a);
    }

    static {
        System.out.println("Child Static 1");
    }

    private int b = 4;

    static {
        System.out.println("Child Static 2");
    }

    Children() {
        super();
        System.out.println("Child Primary Constructor");
    }

    {
        System.out.println("Child Init 2");
        System.out.println(b);
    }

    Children(int a) {
        this();
        System.out.println("Child Secondary Constructor");
    }
}