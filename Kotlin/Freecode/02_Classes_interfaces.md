# Class
Access modifiers are by default public.
- public
- internal - public within module
- private - available withing file where implemented
- protected - only available withing class or subclass

Kotlin uses property access syntax. Access directly by name without getter/setter.
Getters are automatically generated for val - Getters/Setters for var.

## Constructors
Primary and secondary
```
class Person1 constructor(_firstName:String, _lastName:String) {
    constructor(): this("Peter", "Parker") {
        println("secondary constructor")
    }
}
```

## Init blocks
Init blocks are started in order when object is created. Class can have multiple init blocks
```
class Person4 constructor(val firstName:String, val lastName:String) {
    init {
        println("Init1")
    }
    constructor(): this("Peter", "Parker") {
        println("secondary constructor")
    }
    init {
        println("Init2")
    }
}
```
Output is 
```
Init1
Init2
secondary constructor
```
## Initializing field values
### Init blocks
```
class Person1 constructor(_firstName:String, _lastName:String) {
    val firstName:String
    val lastName:String

    init {
        firstName = _firstName
        lastName = _lastName
    }
}
```
### Inline
```
class Person2 constructor(_firstName:String, _lastName:String) {
val firstName:String = _firstName
val lastName:String = _lastName
}
```
Constructor declaration
```
class Person3 constructor(val firstName:String, val lastName:String) {
}
```

## Getter/Setter and method calls
Using set, get you can override default getter/setters, and append additional logic.
```
class Person5 constructor(val firstName:String="Peter", val lastName:String="Parker") {
    // override setter
    var nickName:String? = null
        set(value) {
            field = value
            println("The new nickname is $value")
        }
        get() {
            println("The returned value is $field")
            return field
        }

    fun printInfo() {
        val nickNameToPrint = if(nickName != null) nickName else "no nickname"
        val nickk = nickName ?: "no nickname"
        println("$firstName ($nickNameToPrint) $lastName")
    }

    override fun toString(): String {
        return "Person5(firstName='$firstName', lastName='$lastName', nickName=$nickName)"
    }
}

fun main() {
    val person5 = Person5()
    person5.nickName = "Bo"
    println(person5)
    println(person5.nickName)
    person5.printInfo()
}
```

# Interfaces
```
interface InfoProvider {
    val notValue: String
    fun printInfo()

    fun def() {
        println("Default")
    }
}

interface SessionInfoProvider {
    fun getSessionId():String
}

class BasicInfoProvider: InfoProvider, SessionInfoProvider {
    override val notValue: String
        get() = "Basic Info"

    override fun printInfo() {
        // super.printInfo() - if you wanna call super
        println("Implemented")
    }

    override fun getSessionId(): String {
        // throws exception
        return "SessionId"
    }
}

fun main() {
    val info = BasicInfoProvider()
}
```

# Casting
When casting, you can cast explicitly or kotlin will smart cast
```
interface InfoProvider {...}
interface SessionInfoProvider {...}
class BasicInfoProvider: InfoProvider, SessionInfoProvider {...}

fun main() {
    val info = BasicInfoProvider()
    info.printInfo()
    checkTypes(info)
}

fun checkTypes(infoProvider: InfoProvider) {
    if (infoProvider !is SessionInfoProvider) {
        print("not a session")
    } else {
        println("is session")
        // You can cast it explicitly
        (infoProvider as SessionInfoProvider).getSessionId()
        // or kotlin will smart cast it
        infoProvider.getSessionId()
    }
}
```

# Extending classes and properties
Mark class or field as open.
```
open class BasicInfoProvider: InfoProvider, SessionInfoProvider {
    override val notValue: String
        get() = "Basic Info"

    override fun printInfo() {
        // super.printInfo() - if you wanna call super
        println("Implemented")
    }

    override fun getSessionId(): String {
        // throws exception
        return "SessionId"
    }
}

class ImplementedInfoProvider: BasicInfoProvider() {
    override val notValue: String
        get() = super.notValue
}
```

### Extending fields
Recommendation is to have `open protected fields`. 

```
open class BasicInfoProvider: InfoProvider, SessionInfoProvider {
    protected open val test:String
    get() = "testv"
    
    override val notValue: String
        get() = "Basic Info"
}

class ImplementedInfoProvider: BasicInfoProvider() {
    override val test: String
        get() = super.test
    
    override val notValue: String
        get() = super.notValue
}
```

### Anonymus inner class using object expression
For example a listener 
```
val anonProvider = object : InfoProvider {
    override val notValue: String
        get() = "New info provider"

    override fun printInfo() {
        println("id")
    }
}
```

# Factory using companion object
Companion object is object scoped to the instance of class. Companion obj have access to private stuff. 
Companion keyword can be omitted in java code. But you have to use it in Java or use custom names.

```
interface IdProvider {
    fun getId(): String
}

class Entity private constructor(val id: String) {
    companion object : IdProvider {
        override fun getId(): String {
            return "123"
        }

        fun create() = Entity(getId())
    }
}

class EntityFac private constructor(val id: String) {
    companion object Factory : IdProvider {
        override fun getId(): String {
            return "123"
        }

        fun create() = EntityFac(getId())
    }
}

fun main () {
    val entity = Entity.Companion.create()
    val entity1 = Entity.create()
    
    val entity2 = EntityFac.Factory.create()
}
```
# Object Declaration
Object are thread safe singletons in Kotlin

```
object EntityFactory {
    fun create() = Entitty("123", "Bo")
}

class Entitty(val id: String, val name:String) {
    override fun toString(): String {
        return "id:$id name:$name"
    }
}

fun main() {
    val e = EntityFactory.create()
    println(e)
}
```

# Enums in factory
Enums have property `name`.
```
import java.util.UUID

enum class EntityType {
    EASY, MEDIUM, HARD
    
    fun getFormattedName() => name.toLowercase().capitalize()
}

class Entity constructor(val id: String, val name:String) {
    override fun toString(): String {
        return "id:$id name:$name"
    }
}

object EntityFactory {
    fun create(type: EntityType) : Entity {
        val id = UUID.randomUUID().toString()
        val name = when(type) {
            EntityType.EASY -> type.name
            EntityType.MEDIUM -> type.formattedName()
            EntityType.HARD -> "Hard"
        }
        return Entity(id, name)
    }
}

fun main() {
    val e = EntityFactory.create(EntityType.HARD)
    println(e)
}
```

# Sealed class
Restricted class hierarchies. Class extend base type, but only they can extend it.
For example LoadingState of server. Either server or fail.

Difference between enum and sealed class is sealed class can have different consturctor.

```
import java.util.UUID

enum class EntityType {
    HELP, EASY, MEDIUM, HARD;

    fun formatted():String {
        return name.toLowerCase().capitalize();
    }
}

sealed class Entity () {
    object Help:Entity() {
        val name="Help"
    }

    data class Easy(val id: String, val name: String): Entity()
    data class Medium(val id: String, val name: String): Entity()
    data class Hard(val id: String, val name: String, val multiplier:Float): Entity()
}

object EntityFactory {
    fun create(type: EntityType) : Entity {
        val id = UUID.randomUUID().toString()
        val name = when(type) {
            EntityType.EASY -> "Easy"
            EntityType.MEDIUM -> "Medium"
            EntityType.HARD -> "Hard"
            EntityType.HELP -> type.formatted()
        }
        return when(type) {
            EntityType.EASY -> Entity.Easy(id, name)
            EntityType.MEDIUM -> Entity.Medium(id, name)
            EntityType.HARD -> Entity.Hard(id, name, 2f)
            EntityType.HELP -> Entity.Help
        }
    }
}

fun main() {
    val e = EntityFactory.create(EntityType.HARD)
    val msg = when(e) {
        Entity.Help -> "Help class"
        is Entity.Easy -> "Easy class"
        is Entity.Hard -> "Hard class"
        is Entity.Medium -> "Medium class"
    }
    println(msg)
}
```

## What is data class in sealed
Kotlin way of creating immutable data types. Generates equals, hash, toString. 
Allow doing equality checks on objects. Equality checks can be `==` and based on reference `===`

Class hard is `data` class and equals is autogenerated. If `data` label is removed checking `==` equality will be false.
```
sealed class Entity () {
    object Help:Entity() {
        val name="Help"
    }

    data class Easy(val id: String, val name: String): Entity()
    data class Medium(val id: String, val name: String): Entity()
    data class Hard(val id: String, val name: String, val multiplier:Float): Entity()
}

fun main() {
    val e1 = EntityFactory.create(EntityType.HARD)
    val e2 = EntityFactory.create(EntityType.HARD)
    print(e1 == e2)     // false cause different id

    val e3 = Entity.Hard("id", "name", 0f)
    val e4 = Entity.Hard("id", "name", 0f)
    print(e3 == e4)     // true cause all fields identical
    print(e3 === e4)    // false cause of reference equality
    
    val e5 = e3.copy()
    print(e5 == e4)     // true
}
```

to create copy of object. Use `copy()`. Copy works as builder too, in params you can override properties.
```
e3.copy()
e3.copy("some other id")
```

# Extension functions, extension properties
When you cant control original, but you want to append functionality.
Effective for templated types.
```
fun Entity.Medium.printInfo() {
    print("Medium class: $id")
}
val Entity.Medium.info:String
    get() = "some info"

fun main() {
    val mid:Entity = Entity.Medium("id", "name")
    // doesnt see this cause Entity
//    mid.printInfo()
//    println(mid.info)
    
    // Smart cast
    if (mid is Entity.Medium) {
        mid.printInfo()
        mid.info
    }
}
```