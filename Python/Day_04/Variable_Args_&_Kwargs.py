# Sample case of usage of both *args and **kwargs
# Food Order

def food_order(customer, *items, **extras):
    print(f"Order for {customer}:")

    for item in items:
        print(f"- {item}")

    for key, value in extras.items():
        print(f"{key} : {value}")


food_order(
    "Hari",
    "Pizza", "Veg Panner Roll", "Gobi Manchurian",
    coke = "Pepsi", spice = "Max", delivery = "Home")    