# python uses Mersenne Twister for random
# Module 
import random
import my_module

randInt = random.randint(1, 10)
print(randInt)

randDbl = random.random() * 5;
print(randDbl)

print(my_module.pi)

# List - datastructure
list = ["item1", "item2", "item3", "item4"]
list.append("itemX6")
list.extend(["itemL7", "itemL8"])
print(list)

# Pay for bill
friends = ["Peter", "Jane", "Michael", "Bolton"]
friends = "Peter, Jane, Michael, Bolton".split(', ');
rnd = random.randint(0, len(friends) - 1)
print(friends[rnd])

# IndexError: list index out of range
# friends[6]

# nested lists
list1 = ["list1a", "list1b", "list3c"]
list2 = ["list2a", "list2b", "list3c"]
lists = [list1, list2, "sss"]
print(lists)



