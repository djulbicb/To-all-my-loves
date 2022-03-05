my_tuple = (1, 3, 8)
print(my_tuple)
print(my_tuple[1])

my_list = [1,3,8]

# Razlika izmedju tuple i liste je sto tuple ne moze da se menja jednom kada se zada
# Immutable, constant object
# my_tuple[2] = 12 - Type error
convertToList = list(my_tuple)
