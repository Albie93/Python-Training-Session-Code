#Conditional statement

x = 11
if x == 10:
    print('Equal')

if x > 10:
    print('Greater')
    print('Proceed Next')

if x < 10:
    print('Less')

print('End 1')



import sys  # to terminate program in middle

a = -1
if a>0 and a<=10:
    print('a is Equal')

elif a>10:
    print('a is greater')
    sys.exit()  # to terminate program in middle

else:
    print('a is lesser')

print('End 2')


line = ' '*40
print(line)

#object comparision

s = 'python'
if 'py' in s:
    print('py found')

if s == 'python':
    print('s is equal')


l1 = ['Hello', 'Python']
l2 = ['Hello', 'Python']

#l2 = l1

if l1 == l2:    # == is used to check contents are equal
    print('l1 and l2 are equal')
    

if l1 is l2:    #is operator is used to check reference
    print('l1 and l2 refers to same object')
else:
    print('l1 and l2 points to different objects')

# in and not in operator usage

if 'Hello' in l1:
    print('Hello found')

d = {'name':'ABC', 'roll':20}
if 'name' in d:
    print('Key found')

if 'name' in d.keys():
    print('Key found')

if 20 in d.values():
    print('Value found')

if 200 not in d.values():
    print('Value not found')

if ('roll',20) in d.items():
    print('key and value both found')


# pass

x = 20
if x == 20:
    pass






