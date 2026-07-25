# Topics Covered and Technical Vocabulary
1. Function
2. Function Object
3. Function Call
4. Function Definition(def)
5. Parameters
6. Arguments
7. Local variables
8. Parameter passing
9. Mutation
10. Rebinding
11. Return statement
12. Return value
13. None
14. First-class functions

# Key Concepts
### 1. Functions:
    A function is a named, reusable block of code that performs a specific task.
    Instead of writing same lines of code multiple times, we define it once and call it whenever needed.  

    Functions improve:
        - Code reusability  
        - Maintainability  
        - Modularity  
        - Readability  
        - Testing  
        - Debugging  

### 2. Function Definition (def):
    Python uses the 'def' keyword to define a function.
    
    Ex:
        def greet():
            print("Hello")

    When Python encounters a function definition:
    - A function object gets created.
    - The function name is bound to that function object.

    Here,
          greet --> <function object>
### 3. Function Objects:
    Functions are objects in Python.
    They can be:
    - Assigned to variables
    - Passed to other functions
    - Returned from functions

    Ex:
        welcome = greet
        
        Both refer to the same function object  

        greet   --> <function_object>
        welcome --> <same function_object>

### 4. Function call:
    Simply refering a function is different from executing it.

    greet   --> refer to the function object

    greet() --> The parenthesis '()' tell Python to execute the function object.

### 5. Parameters:
    Parameters are local variables defined in a function that receives objects passed by the caller.

    Ex:
        def greet(name):
            print("Hello", name)

        Here, 'name' is a parameter.  

### 6. Arguments:
    Arguments are the actual objects supplied when calling a function.

    Ex: 
        def greet(name):
            print("Hello", name)

        greet("Krishna")

        Here, 
        "Krishna" --> Argument
        name      --> Parameter

### 7. Local variables:
    Local variables are the variables that include:
    - Parameters 
    - Variables created inside the function body  

    Ex:
        def calculate(price, tax):
            total = price + tax
            return total

        Here, 
        "price" and "tax"          --> Parameters
        "price", "tax" and "total" --> Local Variables         

### 8. Parameter Passing:
    When calling a function, Python does not pass the caller's variable. 
    Instead,
        - A new local parameter variable is created
        - The parameter refers to the same object as the caller's variable

    *** Here, only the object reference is shared not the actual variable

    Ex:
        def greet(name):
            print("Hello", name)

        user = "Krishna"
        greet(user)

        Here, 
            user --> Krishna
            name --> Krishna            
        - Only reference gets passed and both variables refer to same object.

### 9. Mutation:
    Mutation changes the existing object's contents

    Ex:
        numbers = [1, 2, 3]
        numbers.append(4)

        Result:
            [1, 2, 3, 4]

    - The existing list object itself is modified and no new list object gets created.

### 10. Rebinding:
    Rebinding changes which object a variable refers to. 

    Ex:
        def modify(data):
            data = [100]

        numbers = [1, 2, 3]
        modify(numbers)

        Here, 
            Before calling the function:
                numbers --> [1, 2, 3]
            After entering the function:
                numbers --> [1, 2, 3] <-- data
            After executing:
                numbers --> [1, 2, 3]
                data    --> [100]

        - Only the local parameter "data" gets rebound.
        - The variable "numbers" continues to refer to the original list object.
### 11. Return Statement:
    The return statement sends an object back to the caller.

    Ex:
        def add(a, b):
            return a + b

        The function returns the computed object.

### 12. Return Value:
    A function can return any Python Object.
    - Integer
    - Float
    - String
    - List
    - Dictionary
    - Function
    - Class Object

    Ex:
        result = add(10, 20)

        result --> 30
        
        The variable becomes bound to the returned object

### 13. None:
    If the function does not have an explicit return statement, Python automatically returns the special object 'None'.

    Ex:
        def greet():
            print("Hello")

        Here,
        greet() --> returns None

    - None is a real Python Object

### 14. First-Class Functions:
    Python treats functions as first-class objects. This means function can be used like any other object.

    They can be:
    - Assigned to variables
    - Passed as arguments
    - Returned from other functions
    - Stored in collections such as lists and dictionaries

    Ex:
        def greet():
            print("Hello")

        def execute(task):
            task()
        
        execute(greet)

        - Here, the function object referred by greet is passed as an argument without executed immediatley.

        



