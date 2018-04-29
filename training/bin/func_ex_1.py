print('this is a sample')

def add1():
    a = 10
    b = 20
    c = a + b
    print('c =', c)

add1()
add1()

def add2(a,b):
    c = a + b
    print('add2 = ', c)

add2(10,20)
add2(40,50)

def add3(a,b):
    c = a+b
    return c

res = add3(10,20)
print(res)

# function with default arguement
def add4(a,b=10):
    return a+b

print(add4(100))

# multiple arguements are in tuple c
def add5(a,b=10,*c):
    r = a + b
    print('tuple c =', c)
    for i in c:
        r = r + i
    return r

print(add5(10))
print(add5(10,20,30,40,50,60))

# all arguements go in a tuple
def add6(*a):
    print('tuple = ',a)
    r = 0
    for i in a:
        r = r + i
    return r

print(add6())
print(add6(10))
print(add6(10,20))
print(add6(10,20,30,40,50))

# Named arguements while function calling
def add7(a,b=10,*c,d,e):
    r = a + b + d + e
    for i in c:
        r = r + i
    return r

print(add7(10,10,20,30,40,50,d=10,e=10))

# Function with keyword only arguements
def add8(*,a,b):
    return a+b

print(add8(b=10, a=20))

# N number of keyword only arguements will go to a dictionary f
def add9(a,b=10,*c,d,e,**f):
    r = a + b + d + e
    print('tuple =', c)
    print('dict =', f)
    for i in c:
        r = r + i
    for i in f.values():
        r = r + i
    return r

r1 = add9(10,e=20,d=30)
r2 = add9(10,20,30,d=40,e=50,f=60,g=70,h=80,i=90)
print(r2)

# pass by reference
# immutable types
x = 10
y = 20
def add(a,b):
    a = 20
    return a+b

r1 = add(x,y)
print('Add =',r1,x,y)

# mutable types : here l1 will be modified when we change x
l1 = [10,20]
l2 = ['a','b']
def add10(x,y):
    x.append(30)
    return x+y

r1 = add10(l1,l2)
print('add10 =', r1, l1, l2)

# Scope inside functions : scope is local to that function
z = 10
def f1():
    z = 20
    def f2():
        z = 30
        print('z in f2 =', z)
    f2()
    print('z in f1 =', z)
f1()
print('global =', z)

# non local
z = 10
def f1():
    z: int = 20
    def f2():
        nonlocal z # z in f1 will be accessed
        z = 30
        print('z in f2 =', z)
    f2()
    print('z in f1 =', z) #This will change as z is non local.
f1()
print('global =', z)

# Storing function as reference and passing around
def func1():
    print('Inside func1')

    def func2():
        print('Inside func2')

    return func2   #returning func2 without paranthesis

x = func1 # Above function func1 can be stored as a reference in x and passed around
x()
y = func1()
y()

def Account():
    count = 0
    def create_acc():
        nonlocal count
        count+=1
        print('your account no is', count)
    return create_acc

f = Account()
f()
f()

