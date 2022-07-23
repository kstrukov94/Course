# title() и capitalize()
import sys
string1 = sys.argv[1]
string2 = sys.argv[2]
string3 = sys.argv[3]
print(string1.title(), string2.capitalize(), string3.title())

# center()
import sys
string = sys.argv[1]
print(string.center(20).upper())

# подсчет повторений в строке
import sys
word = sys.argv[1]
letter = sys.argv[2]
print(word.count(letter))

#подсчет мужчин и женщин в очереди
import sys
queue = sys.argv[1]
print("m (" + queue.count("m") + ") " + "*" * queue.count("m"))
print("w (" + str(queue.count("w")) + ") " + str("*" * queue.count("w")))




