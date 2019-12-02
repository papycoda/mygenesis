class Animal:
    #class object attribute same for every instance
    species = 'mammal'
    #dog.species not working why???

    def __init__(self,legs,sound,modeOfFeeding):
        self.legs = int(legs)
        self.sound = sound
        self.modeOfFeeding = modeOfFeeding
        print("animal created")
    def eat(self):
        print("i am eating")
    def who_am_i(self):
        print("i am an animal")


class Dog (Animal):
    def __init__(self):
        Animal.__init__(self)
    def who_am_i(self):
        print("i am a dog")

dog = Animal(4,"woof","carnivore")
dog.eat() #this is a method hence the parentheses
Animal.species
print( "the dog goes",dog.sound,Animal.species)#this is an attribute thats why theres no parentheses.
#attributes are like parameters to be filled in,
# while methods are functions to be called to get an action from the class object


class Circle:
    pi = 3.147
    def __init__(self,radius=1):
        self.radius = radius
        self.area = Circle.pi * self.radius**2

    def get_circumference (self):
        return Circle.pi*self.radius*2


my_circle = Circle()
my_circle.pi
my_circle.radius
print("the circumference of the circle is ", my_circle.get_circumference())

class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x1,y1= self.coor1
        x2,y2 = self.coor2
        return ((x2-y2)**2 + (y2-y1)**2)**0.5
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return y2-y1/x2-x1

c1= (3,4)
c2=(4,5)

li = Line(c1,c2)

li.distance()
li.slope()

class Bank():
    def __init__(self,owner,balance=0):
        self.balance = int(balance)
        self.owner = owner
        print("hello,",self.owner ,"what would you like to do today")
    def deposit(self,d_amount):
        self.balance = self.balance + int(d_amount)
        print("you have deposited {} successfully".format(d_amount))
    def withdraw(self,w_amount):
        if w_amount > self.balance :
            print("balance exceeded,please check and retry")
        else:
            print("you have successfully withdrawn {} ".format(w_amount))
            self.balance = self.balance - int(w_amount)
    def __str__(self):
        return "Account name : ", self.owner,"\nAccount balance :#",self.balance


acct_1 = Bank("ope",1000)

acct_1.balance
acct_1.deposit(500)
acct_1.withdraw(5000)







