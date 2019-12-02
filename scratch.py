print("hello testing one two")
import random
print('Hello there, what is your name?')
name = input()

print ("well, {} , I'm thinking of a number between 1 and 10".format(name.upper()))
print ("why don't you take a a guess?")

number = random.randint(1,10)
guesscount = 0
for guesscount in range (1,7):
    guess = int(input())
    if guess < number :
        print("too low, try again")
    elif guess > number :
        print("too high, drop it low")
    else:
        break
if guess == number :
    print("Hooray, you got it")
else:
    print("you' maxed out your chances, the number was {}".format(number))