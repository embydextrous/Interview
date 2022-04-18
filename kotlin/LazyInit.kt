val a: String by lazy {
    println("Hello")
    "Hello"
}

fun main() {
    println(a) // Prints Hello two times as a is being initialized
    println(a) // a is not initialized again so Hello is printed only once
}
