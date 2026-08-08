# Topics Covered and Technical Vocabulary  
1. Multiple parameters 
2. Positional arguments 
3. Keyword arguments 
4. Mixing positional and keyword arguments
5. Default parameters 
6. Default parameter values
7. Function signature
8. Optional parameters 
9. Required parameters 
10. Variable positional arguments(*args)
11. Variable keyword arguments(**kwargs)
12. Tuple
13. Dictionary 
14. Mutable default parameters
15. API design 
16. Backward compatibility 
17. Configuration
18. Validation
19. Normalization

# Key Concepts 
### 1. Multiple Parameters:  
    A function can define multiple parameters to receive multiple objects from the caller.  
    Ex:  
      def add(a, b):  
         return a + b  
    Here, 
    - a, b are parameters 
    - Both are local variables bound to the supplied objects

### 2. Positional arguments:  
    Positional arguments are bound to parameters based on their position.  
    Ex:  
      def introduce(name, age):  
         print(name, age)

      introduce("Ajith", 29)

      Here, 
      - Ajith  --> bound to parameter 'name'
      - 29     --> bound to parameter 'age'

    - Python processes positional arguments from left to right.

### 3. Keyword Arguments:  
    Keyword arguments are bound using the parameter name instead of position.  
    Ex:  
      introduce(age = 23, name = "Ajith")

   Here,  
    - name is bound to "Ajith"  
    - age is bound to 23

    - Order doesn't matter because binding is based on parameter names.

### 4. Mixing Positional and Keyword Arguments:  
    Python allows positional and keyword arguments to be used together.  
    Ex:  
      introduce("Ajith", age = 24)

    Binding occurs as follows:  
    - Positional arguments are bound first
    - Remaining keyword arguments are matched by parameter name.

    * Positional arguments cannot appear after keyword arguments.

### 5. Default Parameters:  
    Default parameters provide predefined objects when the caller does not supply an argument.  
    Ex:  
      def greet(name, message = "Hello"):  
         print(message, name)

    Here, 
    - message defaults to "Hello" if not supplied
    - Passing another value overrides the default

### 6. Function Signature:  
    Function signature defines how a function should be called.  
    It consists of:  
      - Function name
      - Parameters
      - Default values
      - *args
      - **kwargs  

    The signature forms the public interface of a function.

### 7. Optional Parameters:
    Parameters with default values become optional parameters.  
    Ex:  
      def connect(host, port = 8080):  
         ......  
         ......
    Here,  
    - port becomes optional parameter and the caller can omit it.  

### 8. Required Parameters:  
    Parameters without default values are required.  
    Ex:  
      def check_access(user, password):  
         print("Access granted")      

    - Both arguments must be supplied.

### 9. Variable Positional Arguments(*args):  
    *args collects a variable number of positional arguments into a single tuple object.  
    Ex:
      def total(*args):  
         result = 0 

         for num in args:
            result += num

         return result  

      print(total(10, 20))
      print(total(10, 30, 20))
    Here,  
    - All positional arguments are collected into one tuple.
    - The parameter "args" is bound to that tuple.  

### 10. Tuple in *args:  
    Python stores *args as a tuple because:  
    - Function arguments represent caller input.
    - Input should not be accidentally modified.
    - Tuples are immutable
    - Immutabiltiy improves correctness and predictability.

### 11. Variable Keyword Arguments(**kwargs):  
    **kwargs collects a variable number of keyword arguments into one dictionary.  
    Ex:  
       def configure(**kwargs):
         print(kwargs)

         if "timeout" not in kwargs:
            kwargs["timeout"] = 30

         if "temperature" not in kwargs:
            kwargs["temperature"] = 0.7

      return kwargs


      config = configure(
         model="gpt-4",
         temperature=0.2
         )

      print(config)
    Here, 
    - The call:  
      config = configure(  
         model="gpt-4",  
         temperature=0.2  
         )

      Creates a new dictionary for this function call:
   
    - Then,  
      kwargs = {  
         "model": "gpt-4",  
         "temperature": 0.2  
         }

     And the statement,  
      if "timeout" not in kwargs:  
         kwargs["timeout"] = 30

      - adds a new key because timeout is not supplied
   
    - The final dictionary becomes:  
      {  
      "model": "gpt-4",  
      "temperature": 0.2,  
      "timeout": 30  
      }
   
    - Every keyword becomes a dictionary key
    - Every supplied object becomes it's associated value.

### 12. Dictionary in **kwargs:  
    Python generally stores **kwargs in a dictionary becomes keyword arguments naturally represent key-value mappings.

    This allows:
    - Looking up values by key
    - Adding default values
    - Renaming depricated keys
    - Removing unsupported keys
    - Validating and normalizing configuration

### 13. Function creation and execution:  
   def statement  
       ↓  
   creates function object  
       ↓  
   function object knows:  
      - parameters  
      - body  
      - defaults  
       ↓  
   function call  
       ↓  
   actual arguments are supplied  
       ↓  
   parameters are bound to those objects  
       ↓  
   function body executes  
       ↓  
   return object

   * Definition creates the function object. Calling the function creates the execution context and runs the function body.

### 14. Mutable default parameters:  
    Default parameter expressions are only evaluated once when the funtion is defined.

    If the default object is mutable then:
    - The same list object is reused across function calls.
    Ex:  
      def add_item(items=[]):      
         items.append("Apple")
         print(items)

      add_item()
      add_item()
      add_item()

    Output:
      ["Apple"]
      ["Apple", "Apple"]
      ["Apple", "Apple", "Apple"]
    - Why it gives the above output instead of:  
      ["Apple"]  
      ["Apple"]  
      ["Apple"]

    - Because, the function is evaluated only once, when the function is called it executes the function body, so in case of mutable objects, the default object gets overriden.

### 15. API design:  
    Python's parameter system is designed to create and maintain flexible APIs.

    Features such as:  
    - Keyword arguments
    - Default parameters
    - *args
    - **kwargs

    Allows APIs to evolve without breaking existing code.

# Engineering Mode(Why?):
1. Why positional arguments processed before keyword arguments?  

   Python first binds positional arguments from left to right, then binds keyword arguments by parameter name. This avoids ambuigity and keeps argument binding deterministic.  

2. Why do keyword argument exists?  

   Keyword arguments improve readability, maintainability, and allow optional parameters to be supplied without depending on their position.  

3. Why are default parameters only evaluated once?  

   Python creates the default object when it the function object is created, maintaining a consistent object model and avoiding repeated evaluation.

4. Why is *args stored as a tuple?  

   Function arguments represent caller input and should not be accidentally modified. A tuple expresses fixed input through immutability.  

5. Why is **kwargs stored as a dictionary?   

   Keyword arguments naturally form key-value mappings. A dictionary enables efficient lookup and allows frameworks to validate, normalize, enrich, and modify configuration within the current function call.  

6. Why are dictionaries mutable while tuples are immutable?  

   *args represent fixed positional input, whereas **kwargs represent configuration that often needs processing, such as adding defaults, modifying keys, or validating values.  

# Simplified Explanation:

1. What are positional arguments?  

   Arguments that are matched to parameters based on their position

2. What are keyword arguments?  

   Arguments that are matched to parameters based on their names.

3. What are default parameters?  

   Parameters that already have predefined objects if the caller does not provide one.  

4. What is *args?  

   A parameter that collects any number of positional arguments into a tuple.  

5. What is **kwargs?  

   A parameter that collects any number of keyword arguments into a dictionary.  

6. Why is *args a tuple?  

   Because positional arguments represents fixed input and should not be modified accidentally.  

7. Why is **kwargs a dictionary?  
   
   Because keyword arguments naturally represent key-value mapping and dictionary allows efficient configuration processing.

8. Why is a mutable default parameter dangerous?  
    
   Because the same mutable object is reused across multiple function calls, so mutation persist between call.  
