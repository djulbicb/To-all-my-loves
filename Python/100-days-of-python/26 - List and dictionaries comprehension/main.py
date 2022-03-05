old_list = ["one", "two", "three"]
new_list = [item + str(1) for item in old_list]
print(new_list) # ['one1', 'two1', 'three1']

# Comprehension works with all sequences.
name = "Bojan"
new_list = [item + "_" for item in name]
print(new_list) # ['B_', 'o_', 'j_', 'a_', 'n_']

# Assigment
numbers = range(1,10)
new_numbers = [num*2 + num**2 for num in numbers]
print(new_numbers) # [2, 4, 6, 8]

# Comprehension with conditional test
def test(t) :
    return True
def test1(t) :
    return 2
even_numbers = [item for item in numbers if item % 2 == 0]
even_numbers = [test1(item) for item in numbers if test(item)] # [2, 2, 2, 2, 2, 2, 2, 2, 2]
print(even_numbers) # [2, 4, 6, 8]

# Dictionary comprehension
import random
names = ["Bojan", "Ana", "Bob", "Marco", "Theo"]
student_scores = {student:random.randint(0, 100) for student in names}
passed_students = {key:value for (key, value) in student_scores.items() if value > 60}
print(student_scores)
print(passed_students)

# Assigment, word dictionary
sentence = "Hello my name is Bojan"
words = {key:len(key) for key in sentence.split(" ")}
print(words) # {'Hello': 5, 'my': 2, 'name': 4, 'is': 2, 'Bojan': 5}

# Reading with pandas
import pandas
studen_dict = {
    "student" : ["Angela", "James", "Lilly"],
    "score" : [56,76,98]
}
for (key,value) in studen_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(studen_dict)
print(studen_dict)
print(student_data_frame)

for (key,value) in student_data_frame.items():
    print(key, value)

# pandas has built in foreach
for (index, row) in student_data_frame.iterrows():
    print(row.student, row.score, index)
    if row.student == "Angela":
        print("sss")

