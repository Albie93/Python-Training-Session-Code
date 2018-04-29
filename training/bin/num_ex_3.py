n1 = 10
n2 = 12.5
n3 = 0x12
n4 = 0b1010
n5 = 0o12

#Dynamically typed

'''
multiline comment
'''

"""
multiline comment 2
"""

print(n1,n2,n3,n4,n5)
print('n1,n2,n3')
print("n1,n2,n3")
print(type(n1), type(n2), type(n3), type(n4), type(n5))

n1 = 100
print(n1)
n7 = n1
n1 = 200
print(n1,n7)
