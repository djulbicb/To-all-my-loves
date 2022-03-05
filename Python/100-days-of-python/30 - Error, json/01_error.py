# Common errors
# =====================================
# FileNotFoundError
# with open("text.txt") as file:
#     file.read()

# # KeyError
# data = {"key":"value"}
# # data.get("sss")
# data["sss"]

# # IndexError
# fruit = ["Apple", "Bannana"]
# fruit[3]

# # TypeError
# 10 + "s"

# Try catch
# =====================================
try:
    print("Something that can cause an exception")
except TypeError:
    print("if there is a TypeError")
except:
    print("General catch. Do not use bare except.")
else:
    print("Do this if there were NO exceptions")
finally:
    print("Do this no matter what happens")

try:
    with open("text.txt", "r") as file:
        print(file.read())
except FileNotFoundError as error:
    print(error) # [Errno 2] No such file or directory: 'text.txt'
    with open("text.txt", "w") as file:
        file.write("sss")
else:
    # print(file.read()) ne moze ponovo jer je procitano gore
    file.close()

# Example
# =====================================
fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(f"Fruit {fruit}")
make_pie(5)

# Raise Exceptions
# =====================================
if True:
    raise ValueError


