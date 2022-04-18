/**
 * Primary Constructor Called Before Secondary Constructor
 * Constructer called after init block and initializers
 * Init block and initializers called in top to down manner
 * Parent class is called before Child class
 */
open class Parent {
    private val a = println("Parent.a")

    constructor() {
        println("Parent primary constructor")
    }

    init {
        println("Parent.init")
    }

    private val b = println("Parent.b")
}

class Child : Parent {
    val a = println("Child.a")

    init {
        println("Child.init 1")
    }

    constructor() : super() {
        println("Child primary constructor")
    }

    val b = println("Child.b")

    constructor(s: Int): this() {
        println("Child secondary constructor")
    }

    init {
        println("Child.init 2")
    }
}

fun main() {
    Child(2)
}