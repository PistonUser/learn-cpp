import random

b = 1

while b == 1:
	a = random.randint(1,4)
	c = input("stop to stop anything else to continue")
	
	if c == "stop":
		break
	if a == 0:
		print("\n\n")
	elif a == 1:
		print("\n1\n")
	elif a == 2:
		print("\n1\n1\n")
	elif a == 3:
		print("\n11\n")
	elif a == 4:
		print("\n11\n11\n")
