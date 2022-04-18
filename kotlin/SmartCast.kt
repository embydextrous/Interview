class One {
    fun move() {
        println("A is moving")
    }
}

fun main() {
    var a: Any = One()
    if (a is One) {
        // automatically casts to One
        a.move()
    }
    var b: One? = One()
    if (b != null) {
        // Asserts this is not null
        b.move()
    }
}