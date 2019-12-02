#fibbonaci
import pprint,random
n = 50
a,b = 0,1

f = [a, b]
countf = 0

while  countf < n - 2:
    c = a + b
    f = f + [c]
    a,b = b,c
    countf += 1

pprint.pprint("first 50 fibonacci's numbers starting with 0 and 1 are:  " + str(f))
print("Their sum is " + str(sum(f)))

# BINARY GENERATOR
binary = ""
for i in range(4):
    number = random.choice(range(0, 2))
    binary += str(number)
    decimal = int(binary, 2)
print("generated number is : " + str(binary).rjust(4, "0") + " in decimal it's :  " + str(decimal))
