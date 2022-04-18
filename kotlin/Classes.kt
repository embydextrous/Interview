// classes in Kotlin marked as inner are same as Inner classes in Java not marked as static
// inner classes in kotlin not marked as inner are same as inner classes in Java with static keyword
// Inline classes are similar to named tuples and can inherit from interfaces

// Includes impl of toString(), equals(), hashCode(), copy(), and componentN()

// In Java it is PECS (Producer extends Consumer Super), in Kotlin it is POCI (Producer Out Consumer In)
data class Person(val name: String, val age: Int)

sealed class State {
    class Loading : State()
    class Loaded(val data: String) : State()
    class Error(val errorCode: Int) : State()
}

fun main() {
    val person1 = Person("Arjit", 31)
    val person3 = Person("Arjit", 31)
    println(person1)
    println(person1 == person3)
    val person4 = person1.copy(age = 34)
    println(person4)
    println(person1.component1() + " " +  person1.component2())

    // Sealed classes can be used to represent states with different context information
    // Useful for implementing States for UI or any other sort of states
    val state: State = State.Loading()
    when(state) {
        is State.Loading -> { println("Loading") }
        is State.Loaded -> { println("Data is ${state.data}") }
        is State.Error -> { println("Error Code: ${state.errorCode}") }
    }
    printClass("Arjit")
    printClass(2)
    printClass(person1)
}

class Producer<out T>(val value: T) {
    fun get(): T = value
}

// can't declare as property as it can expose
// In Java it is PECS (Producer extends Consumer Super), in Kotlin it is POCI (Producer Out Consumer In)

// This Article - https://medium.com/androiddevelopers/reification-of-the-erased-41e246725d2c
// Why type erasure in Java? For backward compatibility.
class Consumer<in T>(/* val*/value: T) {
    private val producer = Producer(value)
    // can't expose a function outputting T
    //fun get(): T = t
}

//Not Possible Due to Type erasure
//  fun <T> printClass(t: T) {
//      println(t::class.java.simpleName)
//  }

inline fun<reified T> printClass(t: T & Any) {
    println(t::class.java.name)
}

