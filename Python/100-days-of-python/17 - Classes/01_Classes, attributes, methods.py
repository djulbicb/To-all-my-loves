class User:
    pass

user1 = User()
# Attribute is a variable attached to object
user1.id = "001"
user1.username = "Bojan"
print(user1.username)

# Constructor, initializing object
class User:
    def __init__(self, id=0, username="defaultUsername", followers = 0):
        print("Constructor called")
        self.id = id
        self.username = username
        self.followers = followers
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def report(self):
        print(f"Id: {self.id}, Username: {self.username}, Followers: {self.followers}")

user1 = User("01", "Username")
user2 = User()
user3 = User(id=3, followers=10)
print(f"Hello {user1.username}")
print(f"Hello {user2.username}")
print(user3.report())

user1.follow(user2)
print(user1.followers, user2.followers)


