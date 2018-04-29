#Sets

#Collection of items
#Unordered
#No index
#No key
#Main use is it stores unique values
#It is mutable

s = {10, 10, 20, 'Hello', 'Hello'}
print('set = ', s)

#Add
s.add(100)
s.add(100)
print('add = ', s)

#Remove
i = s.remove(100)
j = s.pop()    #this pop is random
print('removed = ', i, j)
print('set = ', s)

#List to set

l = [10,10,20,20]
s = set(l)
l = list(s)
print(l)

