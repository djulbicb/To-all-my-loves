# 01: Basic printing
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')"); # SyntaxError if we forget "
print("print(\"what to print\")") # escape char
print('-----------------------------------')
print("single line\nsecond line"); # new line char
print("hello " + "Bojan");
#  print("IndentationError: unxpected indent"); # white space

# 02: Debugging exercises
print("Day 1 - String Manipulation")
print("String Concatenation is done with the +"+" sign.")
print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and \n."))

# 03: input() function
#name = input("What is your name: ");
#print("Hello " + name);
# Thony aplikacija za debug

# prvo se ispise input funkcija
# posle se ispise print linija
print("Hello " + input("What is your name: "))

#04: Ispisi broj karaktera u inputu
print("Character length of word is: " + str(len(input("Type in your word: "))));

word = input("Type in your word: ");
charCount = len(word);
print("Character length of word " + word + " is " + str(charCount));

#05: Promenljive
name = 10
# print(nama)
# NameError - misstyped variable name

#06: Band name generator
print("Hello to band name generator")
print("----------------------------")
city = input("Where do you want to live?\n")
animal = input("What is your favorite animal?\n")
bandName = city + " " + animal
print("Name of your band should be " + bandName);
