# Higher order functions
Functions that either return functions or take functions as parameter values.

```
fun printString(list: List<String>, predicate: (String) -> Boolean) {
    list.forEach{
        if (predicate(it)) {
            println(it)
        }
    }
}

fun printStringNullable(list: List<String>, predicate: (String) -> Boolean?) {
    list.forEach{
        if (predicate?.invoke(it) == true) {
            println(it)
        }
    }
}

fun main() {
    val list = listOf("Kotlin", "Java", "Javascript")
    // predicate can be placed in and outside of parenthesis
    printString(list, { it.startsWith("K") })
    printString(list) { it.startsWith("K") }

    printStringNullable(list, null)
}
```

 Creating predicate as functions and variables
```
val predicate: (String) -> Boolean = {
    it.startsWith("J")
}
fun getPrintPredicate(): (String) -> Boolean {
    return {it.startsWith("J")}
}
```

# Stream
```
fun main() {
    val list = listOf("Kotlin", "Java", "Javascript")
    list
        .filter{
        it.startsWith("J")
    }
        .map {
        it.length
    }
        .takeLast(1) // Limit to 1
        .forEach{
        println(it)
    }

    // Nullable
    val listNulls = listOf("Kotlin", "Java", "Javascript", null)
    listNulls
        .filterNotNull()
        .filter{
            it.startsWith("K")
        }
        .forEach{
            println(it)
        }

    // Create map from list
    val listMap = listOf("Kotlin", "Java", "Javascript")
    listMap.filterNotNull().associate { it to it.length }
        .forEach{
            println("${it.value}, ${it.key}")
        }

    // get last item
    val languageF = list.filterNotNull().first()
    val languageL = list.filterNotNull().last()
    val language = list.filterNotNull().findLast{it.startsWith("Java")}
    val languageNotFound = list.filterNotNull().findLast{it.startsWith("404")}.orEmpty()
    println(language)
    println(languageNotFound) // null. orEmpty will return "" when null
}
```