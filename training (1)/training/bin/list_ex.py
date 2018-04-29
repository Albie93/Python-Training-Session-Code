#List is mutable

#Create empty list
l = list() # l = []

l = [10, 12.5, 'python', ['a', 'b']]
print('l = ', l)
print(l[2])
print(l[3])
print('Slice = ', l[1:3]) #Slicing is same as that of String.

#List is mutable so we can change items in a list

l[0] = 'Hello'
print(l)
print(l[2][2]) #t
print(l[2][3]) #h
print(l[2][4]) #o

#Append
l.append(100)
print(l)

#Insert
l.insert(2,200)
print(l)

#Merge
m = [1,2,3]
n = ['a','b','c']
k = m + n  #New list will be created
print(k)

#Extend
m.extend(n) #elements of n will be attached to same list m. m will be modified.
print(m)

#Remove

item1 = m.pop()        #pop
item2 = m.pop(1)       #pop with index
item3 = m.remove('a')  #remove particular element
print(item1,item2,item3)
print(m)

m = [10,20,30]
i = m.index(20)
c = m.count(10)
print('i and c', i, c)

#Clear
m.clear()
print(m)

#Reverse
m = [10,20,30]
m.reverse()
print(m)

#Sort (for sorting list should have either numbers or strings. It cant have combination of both.)
p = [10 , 5 , 100]
q = ['d' , 'a' , 'c' , 'b']
p.sort()
q.sort()
print(p)
print(q)
q.sort(reverse = True)
print(q)

#Copying List (Creating a new object as a copy)
#Note: This is a Shallow Copy. Internal references are copied.
r = [10,20, ['a','b']]
t = r.copy()
r.append(30)
print(r)        # [10, 20, ['a', 'b'], 30]
print(t)        # [10, 20, ['a', 'b']]
r[2].append('c')
print(r)        # [10, 20, ['a', 'b', 'c'], 30]
print(t)        # [10, 20, ['a', 'b', 'c']]
r[1] = 300
print(r)         
print(t)

#Deep Copy
import copy
l1 = [10, 20, ['a', 'b']]
l2 = copy.copy(l1)      #Shallow Copy
l1[2].append('c')
print(l1)
print(l2)
l3 = copy.deepcopy(l1)  #Deep Copy. Use function deepcopy.
l1[2].append('d')
print('l1 = ' , l1 , 'l3 = ', l3)



