#strings
#s = ' '
#s = " "
#s = ''' '''
#s = """ """

s = 'person'
print(s)

s = "person's"
print(s)

s = """person's height is 5.9" inches """
print(s)
print(len(s))

#Access indivisual element by using square bracket

print(s[0])

# String objects are immutable. Following will give an error:
# s[0] = 'X'

#Slicing
print(s[2:6]) #startIndex and endIndex . The actual string printed is one index less than endIndex)
print(s[:6])  #Prints from beginning to endIndex
print(s[2:])  #Prints from startIndex till the end
print(s[:])   #Prints entire string
#All above slicing operations are returning NEW string objects.

#Copy to a new string object
t = s  #t and s will point to same string object (Ref Count = 2)
t = s[:] #s[:] will create a new object and t will point to that (Ref Count of t = 1 and Ref Count of s = 1)
s = "Welcome"
print(t)
print(s)

#Contatenation
x = "Hello"
y = "Python"

z = x + " " + y
print(z)

w = y * 10 #Repetition
line = ' ' * 40
print(line)

#Step (Third option is to specify step)
print(z[1:8:1]) #1 is default step
print(z[1:8:2]) #2 is step. So it will print alternate chars starting from first index.
print(z[::1])
print(z[::2])
print(z[::3])

#Step can also have negative values. The traversing direction is from right to left.
print(z[::-1])
print(z[::-2])
print(z[6:1:-1]) #Start and end index positions are changed as traversing direction is from right to left.

#Negative indexes: Strings can also be accessed by negative indexes staring from right to left.
print(z[-1])
print(z[-2])

a = z.startswith('Hel')
b = z.endswith('thon')
print('Starts = ',a,b)
c = z.isupper()
d = z.upper()
print('Upper = ',c,d)
e = z.islower()
f = z.lower()
print('Lower = ',e,f)

c = z.istitle()
d = z.title()
print('Title = ',c,d)

i = z.index('l')    #if not found then Index Error is returned
j = z.find('Z')     #if not found then -1 is returened
print(i,j)

#To remove spaces (Note: We cannot remove spaces from middle)

z = "    Hello     Python     "
k = z.strip()   #removes spaces from both ends
l = z.lstrip()  #removes spaces from left
m = z.rstrip()  #remnoves spaces from right

print(k,l,m)
print(z.isalnum(), z.isdigit(), z.isalpha())

#Split a string

s = "Wel Come"
r = s.split()    #output = ['Wel', 'Come']
t = s.split('e') #output = ['W', 'l Com', '']
print(r)
print(t)

s = "[Welcome]"
x = s.replace('[','X')
print(x)

x = 10
y = 20
z = x + y
res = "addition of {} and {} is {}".format(x,y,z)
print(res)
res = "addition of {1} and {2} is {0}".format(z,x,y)
print(res)

#join

s = 'welcome'
t = ','.join(s)
print(t)   #output = w,e,l,c,o,m,e

