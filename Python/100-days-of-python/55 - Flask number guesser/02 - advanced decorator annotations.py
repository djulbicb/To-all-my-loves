
class User:
    def __init__(self,):
        self.name = ""
        self.is_logged_in = False

def decorate(function):
    def wrapper (*args, **kwargs):
        if (args[0].is_logged_in) == True:
            function(args[0])
    return wrapper

@decorate
def create_blog(user:User):
    print (f"{user.name} is {str(user.is_logged_in)}")

user:User = User
user.name="Bojan"
user.is_logged_in = True
create_blog(user)
