'''
import add_module

print(add_module.msg)
r = add_module.add(10,20)
print('add = ', r)

# give a short name or alias using as
import add_module as am
print(am.msg)
r = am.add(10,20)
print('add = ', r)

# using from
from add_module import msg
print(msg)

from add_module import *
print(msg)
r = add(100,200)
print('r = ', r)

from add_module import msg as m
print(m)
'''

import net.cloud.add_module
print(net.cloud.add_module.msg)
r = net.cloud.add_module.add(10,20)
print('add = ', r)

# give a short name or alias using as
import net.cloud.add_module as am
print(am.msg)
r = am.add(10,20)
print('add = ', r)

# using from
from net.cloud.add_module import msg
print(msg)

from net.cloud.add_module import *
print(msg)
r = add(100,200)
print('r = ', r)

import openpyxl







