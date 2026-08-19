def fruits(items = []):
    items.append("Grapes")
    print(items)

fruits()
fruits()
fruits()

""" 
Output :
['Grapes']
['Grapes', 'Grapes']
['Grapes', 'Grapes', 'Grapes']

"""

#Function gets created once and the code inside the function runs for every function call.
#So, in case of mutable objects, the next function call will have the updated list rather than the default one.
#------------------------------------------------------------------------------------------------------------------

# Safe Mutable Case

def add_items(items=None):
    if items is None:
        items = []

    items.append("Apple")
    print(items)

add_items()
add_items()
add_items()