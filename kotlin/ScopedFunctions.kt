class A {
    var x: Int = 0
    var y: Int = 0

    override fun toString(): String {
        return "A<x:$x, y:$y>"
    }
}

fun main() {
    val a = A().apply { 
        // Object reference using this, returns object on which it is called
        x = 4
        y = 8
    }
    println(a)

    val b = A().run { 
        // Object reference using this, returns result of last statement (in case no result means kotlin.Unit)
        x = 4
        y = 8
    }
    println(b)

    val c = A().let { 
        // Object reference using it (or name), returns result of last statement (in case no result means kotlin.Unit)
        it.x = 4
        it.y = 8
        it.x == it.y
    }
    println(c)

    val d = A().also { 
        // Object reference using it (or name), returns object on which it is called
        it.x = 4
        it.y = 8
        it.x == it.y
    }
    println(d)

    val e = with(A()) {
        // Object reference using this, returns result of last statement (in case no result means kotlin.Unit)
        // Differs with run in one way that this is not an extension function while run is
        x = 4
        y = 8
    }
    println(e)
}