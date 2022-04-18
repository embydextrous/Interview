open class Bases { }

class Deriveds : Base() { }

open class BaseCaller {
    open fun Base.printFunctionInfo() {
        println("Base extension function in BaseCaller")
    }

    open fun Derived.printFunctionInfo() {
        println("Derived extension function in BaseCaller")
    }

    fun call(b: Base) {
        b.printFunctionInfo()   // call the extension function
    }
}

class DerivedCaller: BaseCaller() {
    override fun Base.printFunctionInfo() {
        println("Base extension function in DerivedCaller")
    }

    override fun Derived.printFunctionInfo() {
        println("Derived extension function in DerivedCaller")
    }
}

fun main() {
    // BaseCaller means extension function from BaseCaller is chosen, since call function declares it as type
    // Base it will chose extension function for Base Class - Base class extension function from BaseCaller
    BaseCaller().call(Base())   // "Base extension function in BaseCaller"
    // DerivedCaller means extension function from DerivedCaller is chosen, since call function declares it as type
    // Base it will chose extension function for Base Class - Base class extension function from DerivedCaller
    DerivedCaller().call(Base())  // "Base extension function in DerivedCaller" - dispatch receiver is resolved virtually
    // DerivedCaller means extension function from DerivedCaller is chosen, since call function declares it as type
    // Base it will chose extension function for Base Class - Base class extension function from DerivedCaller
    DerivedCaller().call(Derived())  // "Base extension function in DerivedCaller" - extension receiver is resolved statically
}