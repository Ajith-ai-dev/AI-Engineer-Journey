# 1. Simple function
def greet():
    print("Hello")

greet()

# 2. Binding welcome with greet function
welcome = greet
print(welcome)

# 3. Function with parameters
def show(name):
    print(name)

show("Krishna")

# 4. Function with multiple parameters
def sum(a, b):
    return a + b

result = sum(10, 20)
print("Sum:", result)

# 5. Function with default parameter
def greet(name="Guest"):
    print("Hello", name)

greet("Ajith")
greet()

# 6. Passing a function as an argument
def execute(task):
    task()

execute(greet)    