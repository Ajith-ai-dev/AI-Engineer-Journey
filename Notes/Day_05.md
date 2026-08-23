# Scope, Namespaces, Decorators & Closures 
# Topics Covered and Vocabulary
1. Scope:  
    a. Local Scope  
    b. Global Scope  
    c. Enclosing Scope  
    d. Built-in Scope  
    e. LEGB rule  

2. Namespaces:  
    a. Namespace looking  
    b. Name -> Binding -> Object  
    c. Variable Lifetime  
    d. Name resolution  

3. Closures:  
    a. Closure  
    b. Captured bindings  
    c. Enclosing function lifetime  
    d. Reading enclosing variables  
    e. Mutation through closures  
    f. nonlocal  
    g. Rebinding enclosing names  

4. Decorators:  
    a. First-Class functions  
    b. Function as arguments  
    c. Function as return value  
    d. Nested functions  
    e. Wrapper functions  
    f. Decorator syntax  
    g. @decorator  
    h. *args  
    i. **kwargs  
    j. functools.wraps  

5. Framework Architecture:  
    a. Registration decorators  
    b. FastAPI routing  
    c. Cross-cutting concerns  
    d. Monitoring  
    e. Timing  
    f. Exception Handling  
    g. try / finally  

# Key Concepts
### 1. Scope  
    Scope determines where a name can be resolved.  
    Python follows the LEBG rule  
    L -> Local
    E -> Enclosing  
    B -> Built-In  
    G -> Global  
    Ex:  
        message = "Global"  
        def outer():  
            message = "Enclosing"  

            def inner():  
                message = "Local"  
                print(message)  
            inner()  
        
        outer()  

        output: 
            Local  
            
        - Python finds message in the local namespace first and stops searching  

### 2. Namespaces:  
    Namespace can be thought as a collection of name-to-object bindings.  
    In Python, a namespace is like a box that keeps names (variables and functions) separate so that they don't clash.  

    - A name is bound to an object inside a namespace.  

### 3. Local Scope:  
    Every function execution creates a local execution containing its local bindings. A name created inside a function normally belongs to that function's local scope. This provides isolation.  

    Why?
    - Because allowing every function to directly modify the same names would create unneccesary coupling and unpredictable side effects. Local scope therefore helps with:
        a. Encapsulation
        b. Isolation  
        c. Maintainability  
        d. Prevents accidental changes  

### 4. Global Scope:  
    Names defined at the module level belong to the global namespace of that module.  

    Functions can read the global names when they don't have a matching local or enclosing binding.  

    However, relying heavily on global mutable state can make software hard to reason about.

    Engineering Insight:  
        - Global state is not automatically bad, but unnecessary share mutable state increases coupling.  
        - In production systems, configuration and state should generally have clearly defined ownership.  

### 5. Enclosing Scope:  
    An enclosing space exists when there are nested functions.  

    If a function is defined inside another function, the outer function's namespace becomes the "enclosing namespace" for the inner function.  

    This gives the inner function access to the named defined in the outer function. This mechanism is the foundation for closures.  

### 6. Built-in Scope:  
    The built-in namespace contains names provided by Python itself.  
    Some commonly avalaible functions are:  
    - print  
    - len  
    - type  
    - id  

    If Python cannot a find a name in the local, enclosing, or global namespaces, it eventually checs the built-in namespace.  

### 7. LEGB Rule:  
    Python uses the LEGB rule for name resolution.  

    Local
      |  
      V  
    Enclosing  
      |
      V  
    Global  
      |
      V  
    Built-in

    When Python encounters a name, it searches scope in order. The first matching binding determines which object the name refers to.  

    Why?  
    - Without a predictable lookup order, nested functions and local variables becomes difficult to reason about. LEGB provides a mechanism for resolving names.  

### 8. Nested Functions:  
    Python allows functions to be defined inside other functions.  

    Nested functions can be useful when apiece of logic:  
    - Is only relevant to the outer function  
    - Needs access to the outer function's state  
    - Is being used to construct another function  
    - Is part of a decorator  

    Nested function provide a mechanism for localizing behavior and state.  

### 9. Closures:  
    A closure is created when a nested function retains access to bindings from its enclosing scope.  
    
    Normally, we expect the local state of a function to be inaccessible after that function finishes. However, if a nested function still needs access to enclosing binding, Python allows that relationship to be available.  

    "A closure allows a function to retain access to bindings from it's enclosing scope".  


    ** Why Do Closures Exist?  

    Closures allows functions to carry context or state without depending on Global variables.  

    They are useful when we want the function to remember something about the environment in which it was created.  

    Uses cases:  
        - Function factories  
        - Callbacks  
        - Stateful functions  
        - Decorators  
        - Framework Internals  

### 10. Reading, Mutability and Rebinding in Closures:  
    






        
    

