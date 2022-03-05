
class User:
    def __init__(self, name="", surname="", email="", password="", registered=""):
        self.name = name
        self.surname = surname
        self.email=email
        self.password = password
        self.registered = registered

    def __repr__(self) -> str:
        # Prints as json
        return f"{self.__dict__}"
