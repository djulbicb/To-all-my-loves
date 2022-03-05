def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

# Prioritet, ide od dole na gore
@make_emphasis
@make_bold
def blog():
    return "test"

x = blog()
print(x)