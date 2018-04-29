#classes

#class is a collection of variables and functions. A function is also a collection of sub functions and variables.
#classes have follwing advantage over functions:

#multiple objects
#inheritance
#operator overloading

class Company:

    #Class variable. Common to all objects. Hence called by ClassName.VariableName. Same as static variables.
    c_code = 123

    # method which is having 'self' is instance method
    def set_comp_name(self,n):
        self.c_name = n         #this is an instance variable setter.

    # this is an instance method as it has 'self' in it.
    def get_comp_name(self):
        return self.c_name      #this is an instance variable getter.

    #Class method: This is a class method as it does not have 'self' in it. Called directly by ClassName.MethodName. Same as static methods.
    def govt_rules():
        s = "rules"
        return s

c1 = Company()
c2 = Company()

c1.set_comp_name('Syne')
c2.set_comp_name('XYZ')

r1 = c1.get_comp_name()
r2 = c2.get_comp_name()

print('r1 = ', r1, 'r2 = ', r2)
print(Company.c_code)
print(Company.govt_rules())

#Inheritance : Creating a sub class

class Team(Company):

    # __init__ is constructor
    def __init__(self):
        self.t = []

    def add_emp(self,n):
        self.t.append(n)
        return self.t

    def sample(self):
        self.x = 'X'

t1 = Team() #__init__ will be called to initialise the object
t1.set_comp_name('Oracle')
r1 = t1.get_comp_name()
t1.add_emp('A')
print(t1.t)

# This will give error as member variable x is not initialised by any function
#print(t1.x)

# Initialise / assign value to a member variable x
t1.sample()
# member variable x can be accessed ONLY AFTER it is being initialised by sample function
print(t1.x)

#Access class methods of Company class by Team
Team.govt_rules()
Team.c_code

#Multi Level Inheritance

class New_Team(Team):

    #method overidden
    def add_emp(self,n):
        self.t.append(n)
        return self.t

    def __init__(self):
        super().__init__()

    def f1(self):
        print("New_Team f1")

n1 = New_Team()
r = n1.add_emp('B')
print('emp list = ', r)
        
#Multiple inheritance

class Loc:

    def addLocation(self,n):
        self.location = n
        return self.location

    def f1(self):
        print("Loc f1")

class MyTeam(New_Team, Loc):
    def msg(self):
        return 'Hello'

m1 = MyTeam()
m1.set_comp_name('Synec')
r = m1.addLocation('Pune')
print('loc = ', r)
#same function is present in both parents New_Team and Loc. f1 in New_Team is called.
#The interpreter searches for method from left(entire heirarchy) to right.
#So from New_Team to Loc is direction of serching the method.
m1.f1()


#composite object
class SomeTeam:
    def __init__(self):
        l1 = Loc()          # l1 is not a composite object
        self.l2 = Loc()     # Here l2 is composite object as it is linked using 'self'

    def someMsg(self):
        pass

s1 = SomeTeam()
s1.someMsg()

