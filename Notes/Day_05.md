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
    A Closure can access an enclosing binding.

    Reading:  
    Reading an enclosing name is allowed. The nested function simply retrieves the object associated with that binding.  

    Mutation:  
    If the binding refers to a mutatable object, the nested function can mutate that object.  
    The binding itself remains unchanged.  
    - Ex: adding an item to an existing list changes the list object, not the name-to-object relationship.  

    Rebinding: 
    Rebinding means changing the object a name refers to. In closures, to rebind inside a nested function, Python requires the keyword 'nonlocal'.  

### 11. nonlocal:  
    nonlocal is a keyword in Python. It tells Python that the name belongs to enclosing function scope.  
    
    This allows the nested function to rebind the existing variable instead of creating a new local variable. This is helpful in maintaining state inside closures.  

    * Without nonlocal, Python assumes the name is a local variable and assigns the object reference.  

    Ex:  
        def outer():  
            count = 0  

            def increment():  
            nonlocal count
            count += 1  
            return count

            return increment

        
        counter = outer()   
        print(counter())  
        print(counter())  

    Output:  
    1  
    2

### 12. First-Class Functions:  
    Python functions are objects. Therefore, functions can be:  

    - Passed as Arguments  
    - Assigned to names  
    - Returned from functions  
    - Used by other functions  
    - Stored in data structures  

    This is called first-class function support and this is directly connected to decorators.  

    Why?  
    A decorators needs to receive a function, potentially create a function and return a function, without first-class function it will be harder to implement.  

### 13. Decorators:  
    A decorator is a mechanism for extending or modifying the existing behaviour of the function without changing the function's core implementation.  

    Mental Model:  
    
    Original function  
            |  
            V  
        Decorator  
            |  
            V  
    New / Modified callable  

    The @decorator syntax is simply a convenient way of expressing function transformation or registration.  

    Here, a function object is passed to a decorator and the resulting function object is bound to the decorator name.  

### 14. Wrapper functions:  
    A common decorator pattern creates a wrapper function around the original function.  
    The wrapper can perform additional work before or after the original function call.  

    Caller  
       |
       V  
    Wrapper  
       |  
       V  
    Original Function  
       |  
       V  
    Result

    The wrapper can therefore add behaviour without modifying the original function's implementation.  

    Typical behaviour includes:  
    - Logging  
    - Timing  
    - Authentication  
    - Validation  
    - Monitoring  
    - Error Handling  
    - Caching  

### 15. *args and **kwargs in Decorators:  
    A decorator should ideally be reusable across functions with different signatures.  

    A wrapper therefore commonly accepts:  

    Variable positional arguments through *args  
    Variable keyword arguments through **kwargs  

    The wrapper can then forward those arguments to the original function.  

    Engineering Insight  

    This allows a generic decorator to work with many different APIs without knowing their exact signatures beforehand. This is an example of interface flexibility.  

### 16. functools.wraps:  

    A wrapper technically replaces the original function binding. This can cause metadata associated with the original function to become less visible.  

    For example, the function's:  
        - Name  
        - Documentation  
        - Other metadata  
        can appear to belong to the wrapper instead.  
    
    functools.wraps helps preserve important metadata from the original function.  

    Why?  
    Because changing a function's behavior should not unnecessarily destroy information that developers, debugging tools, documentation systems, or frameworks may depend upon.

### 17. Decorators and Frameworks:
    Decorators are not just a Python convenience.  
    
    They are heavily used by frameworks.  
    
    For example, a web framework can associate a function with a route through a decorator.
    
    Conceptually:  
    
        Function  
            ↓  
        Decorator  
            ↓  
        Framework registration  
            ↓  
        Routing metadata  

    The framework can then maintain a mapping between an external event and a Python function.  
    
    For an AI API, this might conceptually become:  

        POST /predict  
            ↓  
        predict()  
            ↓  
        Preprocessing  
            ↓  
        Model inference  
            ↓  
        Response  

    This is one reason understanding Python decorators is important before working deeply with AI frameworks.



    






        
    

