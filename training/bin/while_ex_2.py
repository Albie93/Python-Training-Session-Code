# while loop

# if True:
# if 0: False
# if non-zero: True
# if False:

x = 10
while x > 0:
    print(x)
    x = x - 1

line = '#'*40
print(line)

s = 'Hello'
i = 0
while i < len(s):
    print(s[i])
    i+=1

print(line)

l = [10,20,30]
while l:        #if element is there in l it will return true
    x = l.pop()
    print('x = ', x)

print(line)

d = {'A':10, 'B':20}
while d:        #if element is there in dictionary it will return true
    x = d.popitem()
    print('x = ', x)

print(line)

'''
#Accept input from console with input

cart = []
while True:
    item = input('Enter Item:')
    cart.append(item)
    ch = input('Do you want to quit?(y/n)')
    ch = ch.upper()
    if ch == 'Y':
        print('cart =', cart)
        break

'''

comp = ['sap', 'syne', 'IBM']
j = 0
while j < len(comp):
    if comp[j] != 'syne':
        j+=1
        continue
    print('End of while')
    j+=1

print(line)





