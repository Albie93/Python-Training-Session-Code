import os
import subprocess as sb
l1 = os.listdir()
l2 = os.system('dir')
if l2 == 0:
    print('success')
    r = sb.call('dir', shell = True)
    print('Output is', r)
