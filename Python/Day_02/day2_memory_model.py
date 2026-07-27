print("==== Binding and Rebinding ====")

a = 100
print(f"a: {a}")

b = a
print(f"b: {b}")

a = 125

print("After rebinding a to 125")
print(f"a: {a}")
print(f"b: {b}")

print("\n==== Shared References ====")

numbers = [10, 20]
backup = numbers

backup.append(30)

print("numbers:", numbers)
print("backup :", backup)

print("\n==== Mutation vs Rebinding ====")

numbers = [1, 2]
backup = numbers

backup = backup + [3]

print("numbers:", numbers)
print("backup: ", backup)

print("\n==== Object Identity ====")

a = [1, 2]
b = a
c = [1, 2]

print(id(a))
print(id(b))
print(id(c))

print("\n==== Equality vs Identity ====")

print(a == b)
print(a is b)

print(a == c)
print(a is c)

