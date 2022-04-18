/*
 * Numbers are stored as primitves except in case of generics and Int?
 */

/*
Kotlin also has classes that represent arrays of primitive types without boxing overhead: ByteArray, 
ShortArray, IntArray, and so on. These classes have no inheritance relation to the Array class, but 
they have the same set of methods and properties.
 */

fun main() {
    val a: Int = 100
    val boxedA1: Int? = a
    val boxedA2: Int? = a

    // returns true - Integer Cache Comes to picture which is 1 byte in size -128 to 127
    println(boxedA1 === boxedA2)

    val b: Int = 10000
    val boxedB1: Int? = b
    val boxedB2: Int? = b

    // returns false as b is out of integer cache
    println(boxedB1 === boxedB2)
}
