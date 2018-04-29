#Tuple
#Tuple is immutable. It is similar to liist.

t = (10, 12.5, 'python', ['a', 'b'], (10, 20))
print(t)
print(t[0])
print(t[1:2])

# t[0] = 200 This wont work as tuple is immutable

i = t.index(12.5)
c = t.count(10)
print(i,c)

#A tuple with one element is denoted as (10,)

x,y = (10, 20)
z = (10)            
print(type(z))      # class int
z = (10,)
print(type(z))      #class tuple

# Use class name to interconvert between types

a = 10
b = str(a)
c = int(b)
d = [10,20]
e = tuple(d)
f = list(e)

s = 'welcome'
l = list(s)
print('l = ', l)
m = ''.join(l)
print(m)
