from datetime import time

t = time(14, 59, 36, 9955)

print(t)

print(t.hour, t.minute, t.second, t.microsecond)

print(t.replace(15))
