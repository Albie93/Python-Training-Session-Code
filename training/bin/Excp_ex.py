
a = 10
b = 0

try:
    c = a/b
    print('c = ', c)
except:
    print('some error')

line = '-'*40
print(line)

# Specifying classes
a = 10
b = 0

try:
    c = a/b
    print('c = ', c)
except ZeroDivisionError:
    print('zero division error')
except NameError:
    print('name error')

line = '-'*40
print(line)


# finally
g = 10
h = 0

try:
    r = g/h
except Exception as a:
    print('Some Error', type(a))
    #r = g/h
finally:
    print('Finally block')



# Throwing Errors
i = 10
j = 0

try:
    if j == 0:
        raise ZeroDivisionError
    r = i/j

except:
    print('some error')


#Assertion 
m = 10
n = 0

try:
    assert n>0 , 'Invalid Number !!!'
    r = m/n
except AssertionError as a:
    print('Assertion error = ', a)


import bottle


