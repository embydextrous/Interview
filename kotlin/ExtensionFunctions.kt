open class Base {
    fun move() {
        println("Class Move")
    }
}

class Derived : Base()

fun Any.print() {
    println("Any")
}

fun Base.print() {
    println("Base")
}

// extension property
val Base.value: Int
    get() = 12

fun Base.move() {
    println("Extension Move")
}

fun Derived.print() {
    println("Derived")
}

fun main() {
    val derived: Base = Derived()
    // Extension functions are resolved at compile time and since derived is explicity declared as Base
    // it prints Base
    // If No extension function is present for Base classes it will look for extension function for super
    // classes and use them. If not found will throw compilation error.
    derived.print()

    val derived2 = Derived()
    // Here it will print Derived as type inferred will be Derived
    // However is no extension is defined for derived it can look for extension function in of super classes
    derived2.print()

    // if same extension and member available - member wins
    derived2.move()

    println(derived.value)
}