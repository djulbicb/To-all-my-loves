# Not a programmer of code, but a programmer of bugs :D
# Every bug you fix is like flexing muscles

# Replit posle izvrsavanja koda, zadrzavana u memoriji vrednosti pa koristi konzolu da vidis .... tip vrednost....

# 01 Kad naidjes na problem, probaj da opises problem.
    # onda testiraj tvoje pretpostavke da vidis koja je netacna
# Describe Problem
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# 02 Reproducing the bug
    # Primer je randint(0,6)... Umesto toga hardcode na 6 pa ce uvek da baca error
# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# 03 Stavi se u ulogu kompjutera
# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# 04 Fix error, kada ti konzola nesto kaze
# Tipa expected indented block, ili TypeError
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")

# 06 Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # ova ima ==
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)

# 07 Debugger
# https://pythontutor.com/visualize.html#mode=display0
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    #   b_list.append(new_item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# 08 Take a BREAK :)

# 09 Ask a Friend

# 10 Run often

# 11 Ask stackoverflow