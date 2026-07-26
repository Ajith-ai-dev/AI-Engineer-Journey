# Topics Covered and Technical Vocabulary
1. Objects
2. Variables
3. References
4. Binding
5. Rebinding
6. Mutable Objects
7. Immutable Objects
8. Mutation
9. Object Identity(id())
10. Equality(==)
11. Identity(is)
12. Shared References
13. Side Effects

# Key Concepts
### 1. Objects:
   An object is an entity created by Python that stores the actual data in memory. Every value in Python (lists, dictonaries, integers, functions etc) is an object.
     
     Ex:
        10,
        "Hello"
        [1, 2, 6]

### 2. Variables:
    A variable is a name that refers to an Object. Variables do not store values directly.
     
     Ex:
        x = 10
        Here, x refers to the integer object 10.

### 3. Binding:
    It is the process of associating an object to a variable.
     
     Ex:
        a = 10
        Here, a is bound to the integer object 10.

### 4. Rebinding:
    Rebinding changes the variable so that it refers to a different object.
     Ex:
        a = 10
        a = 100 
    - The variable a now refers to the integer object 100
    - The object 10 remains as it is(unaffected)

### 5. Mutable Objects:
    Mutable Objects are the objects that can be modified after creation.
     Ex:
    - Lists
    - Dictionaries
    - Sets
     Ex:
        numbers = [10, 20]
        numbers.append(30)
        - Now, numbers is [10, 20, 30]
        The existing list object is modified.

### 6. Immutable Objects:
    Objects that cannot be modified after creation.
    - int
    - string
    - tuple
    - bool

    Ex:
       name = "Arjun"\
       name = "Krishna"

    Python creates a new string object 'Krishna' instead of overriding Arjun, this rebinds the name with the new string object.

### 7. Mutation:
    Mutation changes the contents of the existing object

    Ex:
        names = ["Hari", "Ram", "Krishna"]
        names.append("Kalki")
        
        No new list object is created, the existing list changes.

### 8. Rebinding vs Mutation:
    In rebinding, the variable is rebound with a different object, and the old object remains unchanged while a new object gets created.        

    In Mutation, the existing objects changes and no new object gets created.

    Ex:
        a = 10\
        a = 100

        This is rebinding and new object 100 gets created.

        names = ["Ram", "Krishna"]
        names.append("Parasurama")

        This is mutation, the existing object changes.

### 9. Object Identity (id()):
    In Python, every object has a unique identity during its lifetime, here it is typically the object's memory address.
    id(object) --> gives the address of the object

### 10. Equality( == ):
    Equality operator compares object contents(values).
    
    Ex:
        [1, 2, 3] == [1, 2, 3]
        
        This results to "True". Comparision gives a boolean result of True or False.

### 11. Identity( is ):
    "is" checks whether two variables refer to the same object location.

    Ex:
        a = [10, 20, 3]
        b = a
        a is b --> Returns True

### 12. Shared References:
    In Python, multiple variables can refer to the same object.

    Ex:
        even_numbers = [2, 4, 6]
        even = even_numbers

        In case of list, mutating of one reference affects others because all the variables point to the same object.

# Engineer Mode(Why?):
1. Why lists are mutable?  
   Lists are designed to be updated frequently. Mutability avoids creating new list whenever an element is added or removed, this improves efficiency for dynamic collections.

2. Why strings are immutable?  
    Strings are widely shared throughout programs. Immutability prevents accidental modifications, making programs more predictable, safer, and easier to maintain or reason.

3. Why Python provide "==" and "is", if both are used for comparision?
   - "==" compares the actual contents of the object (compares object itself)
   - "is" compares the location that the object is pointing to.
   - The main difference is that:
    Ex:
        a = [10] 
        b = [10]
        print(a == b) --> True
        print(a is b) --> False

    - Identity checks are much faster because Python compares only object identities instead of actual contents.

# Code Snippets:
    a = 10            #Binding
    a = 20            #Rebinding
    b = a
    numbers = [1, 2]
    numbers.append(3) #Mutation
    a == b            #Equality
    a is b            #Identity
    id(a)             #Object Identity 
    
# Simplied explanation:
1. What is an object in Python?  
    An object is a piece of data created by Python. Variables don't store the data itself; they refer to objects that hold the data.