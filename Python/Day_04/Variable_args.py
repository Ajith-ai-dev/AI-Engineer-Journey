# Passing variable length arguments, in case of Variable Length arguments, always the passed input is a tuple.

def total(*args):
    print("args:", args)
    print("type:", type(args))
    result = 0
    for number in args:
        result += number

    return result

print(total(10, 20))
print(total(20, 210, 1))
print(total(1, -2, 2))