#В английском языке приняты следующие сокращения:
#I am — I'm
#You are — You're
#He is — He's
#She is — She's
#It is — It's
#We are — We're
#They are — They're
#Напишите программу, которая получает из первого аргумента командной строки фразу на английском языке,
# а затем заменяет в ней все полные сочетания на сокращения (в соответствии со списком выше).

import sys
string = sys.argv[1]
string = string.replace("I am", "I'm").\
    replace("You are", "You're").\
    replace("He is", "He's").\
    replace("She is", "She's").\
    replace("It is", "It's").\
    replace("We are", "We're").\
    replace("They are", "They're")
print(string)
