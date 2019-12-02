for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

tt = ' print every word that start with s '
for word in tt.split():
    if word[0] == 's':
        print(word)


def capo(another):
    first = another[0]
    ikeji = another[1:3]
    ikerin = another[3]
    iyoku = another[4:]
    print(first.upper() + ikeji + ikerin.upper() + iyoku)


another = input('enter your cap word: ')
capo(another)


def yoda(text):
    rvr = text.split()
    rwl = rvr[::-1]

    print(' '.join(rwl))


tbrv = input('enter your yoda word: ')
yoda(tbrv)
