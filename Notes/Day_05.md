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

    If a function is defined inside another function, the outer function's namespace becomes the **enclosing namespace** for the inner function.  

    This gives the inner function access to the named defined in the outer function. This mechanism is the foundation for closures.      


        
    

