# Variable Length Keyword arguments is a Python design that helps in passing multiple keyword based mapping values
# In this case, the input is a dictionary(dict), mutation is allowed in this design.

def configure(**kwargs):
    print("kwargs:", kwargs)
    print("Type:", type(kwargs))

configure(
    model = "GPT-5.0",
    temperature = 0.8,
    max_tokens = 500
)