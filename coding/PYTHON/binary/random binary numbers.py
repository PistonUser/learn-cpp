import random

t = 0
number = ""

while t != 8:
    number = number + str(random.randint(0,1))
    t = t + 1
print(number)