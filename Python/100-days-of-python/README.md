# 100-days-python

for debugging
https://pythontutor.com/visualize.html#mode=display
thorny

djulbic.bojan@gmail.com

| Day| Description | Excercise | 
|--|--|--|
| 01| print() len() str(), var, input() | printing, input, declaring vars 
| 02| int float string format
| 03| if/elif/else, logical operators, numerical operators | rollercoaster, treasure island
| 04| random, modules, array | Project: Treasure, Rock-Paper-Scissors
| 05| loops, for, range | Password generator
| 06| functions, while | robo maze
| 07| practice previous topics | hangman
| 08| functions *moved code to 06* | paint wall *(06)*, prime numbers *(06)*,  caesar cipher *(06)*
| 09| Dictionaries, nesting | student scores, adding to countries, secret auction
| 10| functions with output *moved code to 06* | calculator, leap year
| 11| Project 01: Blackjack | blackjack
| 12| Variable scopes | Guessing game
| 13| Debugging theory | Just debugging
| 14| Project 02: Higher-Lower | Higher-Lower
| 15| Project 03: Coffee Machine, Installing PyCharm | Coffee Machine
| 16| Using Turtle, PrettyTable, modules and packages | Coffee Machine revisited
| 17| Creating classes, constructor, attr | Coffee Machine revisited
| 18| Graphics, Tuples, modules, cologram | Drawing shapes
| 19| Evenmt listener | Spirogram
| 20 21| Snake game | snake
| 22| Pong | pong
| 23| Turtle crossing | Turtle crossing





- coding is like open book exam. Remember only how things work and search for rest
- Gotta keep trying. Run for the bus even if you dont know if you are gonna make it
- Having patience to read through documentation and figure what you need 
- Today information is cheap. Google. Your job is to understand the code.
- Ovo je maraton. Zasto zelis ovaj goal. How much you want that goal? Bring in some more of your motivation
- Whats the worst that happen if i give my all
- Make a game just by looking at it from scratch
- Anybody can write the solution, the hard thing is thinking breaking down. Logic. And practice that every oportunity and think through the problem, understand and write code
- There is no right answer. 

`

Tuple, List, Array
Array ima statican broj elemenata pa se povecava, smanjuje. Neefikasno memorijski
List - LinkedList, DoubleList. Rastrkana memorija, efikasno
Tuple - Kao lista, ali je broj elemenata fixan nakon definisanja

# pythonanywhere
cloud server for python

import java.awt.*;
import java.awt.event.KeyEvent;

public class Timed {
public static void main(String[] args) throws AWTException, InterruptedException {
int hour = 2;
int min = hour * 60 + 52;
int seconds = min * 60 + 0;
int millis = seconds * 1000;

        Robot robot = new Robot();
        Thread.sleep(millis);
        robot.keyPress(KeyEvent.VK_CONTROL);
        robot.keyPress(KeyEvent.VK_F10);
        robot.keyRelease(KeyEvent.VK_CONTROL);
        robot.keyRelease(KeyEvent.VK_F10);
    }
}


# Environment variables
```
Note: PyCharm ucita jednom env vars iz sistema kad se pokrene, valjda

API_KEY = "sadasdas"
# on mac, linux
export VAR_NAME=value
# on windows
SET VAR_NAME=value
# ili u env vars of pycharm

import os
api_key = os.environ.get("VAR_NAME")
print(api_key)

---
Set env var


APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
```



pip install BeautifulSoup4
http://myhttpheader.com/