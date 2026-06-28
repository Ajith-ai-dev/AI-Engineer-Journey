# Topics Covered
- 1. What is SDK(Software Development Kit)?
- 2. Why Python is widely used than C++ even though the latter being the fastest?
- 3. How to create and run a Python program?
- 4. What is the difference between = and ==?
- 5. What does print() do?

# Explanations
1. SDK (Software Development Kit) is a collection of tools, libraries, documentation, and sample code that help the developers in developing  software applications.

2. Python is the most widely preffered language than C++ even though Python is slow because:
    - Development is much faster in Python, as C++ needs lots of lines and setup. And as AI is all about expermentation and deployment of code, Python's less code syntax is more helpful for developers over execution speed.
    - Python has rich libraries like PyTorch, Scikit-learn, TensorFlow which is significant for AI development. One note is that internally all these libraries uses C++ which means faster execution time.
    - Python has the largest online community and shared knowledge platforms like GitHub repos, tutorials and research papers. This improves problem solving.
    - Python excels at integrating with other technologies and libraries, making it suitable for building end-to-end AI applications. 

3. In visual studio code, you can right click on your git initilised folder and create a new file, 
    In terminal,
    - touch hello.py to create a file
    - python hello.py to execute the file

4. In Python, 
    - '=' represents assignment, it assigns the value on right-hand side to the variable on the left-hand side.
    - '==' represents comparison operation, it compares the values on both sides. 
        - If both are equal, it returns 'True'
        - If both are not equal, it return 'False'

5. print() in Python, is a built-in function that displays value in the console.

# Key Concepts
1. Variable : A name used to refer a value so that we can use or modify it later in the program. Basically a container used to    store values
    - Ex:
    name = "Krishna"
    Here, name is the variable and it refers to the string object 'Krishna'

2. '=' : Assignment Operator, used to assign values to variable
3. '==' : Comparison Operator, used to compares values, it always return either True or False
4. print() : A built-in function that is used to display values to the console

# Doubts and responses
1. Why Git doesn't track empty folders?
    - Git only tracks files so creating a folder that is empty will not have anything to track. Programmers create an empty file '.gitkeep', which can be used to commit and push to track folders. When we actually create a file then this file can be removed

# Technical Vocabulary
1. Repository: A Git Project
2. Branch: An independent line of development in a repo
3. Expression: Code that evaluates to a value
4. Statement: An instruction executed by Python
5. Function: A reusable block of code that performs a specific task

# Code Snippets
1. name = "Hari"
   print(name)
2. age = 10
   print(age)       -- 10
   print(age == 10) -- True
   print(age = 10)  -- Syntax error
3. a = 10
   b = 20
   a = b
   b = 30
   print(a) -- 20, comparison operator will not re-assign the value to the variable it just evaluates the expression

# Improvements and suggestions
1. Always be consistent in using quotes use "" or '', do not use '' in one place and "" in another even though both are correct.