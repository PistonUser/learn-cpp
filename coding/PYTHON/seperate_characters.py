import string


string = str(input())
lasti = ""
numofnum = 1
numA = "0"
suma = 0
for i in string:
    if i == " ":
        numofnum += 1
        suma += int(numA)
    if i != " ":
        numA = lasti + i
    lasti = i
else:
    suma += int(numA)
print(suma)