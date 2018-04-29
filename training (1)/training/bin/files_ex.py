# Files

f = open(r'c:\training\log\out1.txt', 'w')

#Wonly
#Existing data will be erased

x = 10
y = 20

x = str(x) + '\n'
y = str(y) + '\n'
#write function only accepts strings as input arguements
f.write(x)
f.write(y)

l = [x,y]
f.writelines(l)

# if we close file we cannot write data to a closed file.
#f.close()

#Use flush to transfer data from buffer to actual file.
f.flush()

f.write(x)

f.flush()

f.close()

#if we not passing second arguement then by default file is opened in read only mode
#f = open(r'c:\training\log\out1.txt')
f = open(r'c:\training\log\out1.txt', 'r')

res1 = f.read()
print(res1)

#We need to reset the seek pointer to starting position
f.seek(0) #use f.seek(0,2) to take cursor to end of file

res2 = f.read()
print(res2)

f.seek(0)
res3 = f.readline() #reads one line at a time
print(res3)

f.seek(0)
res4 = f.readlines() #read all lines and return result in a list.
print('res4 = ', res4)

#convert read result from string to respective type
f.close()
a = res4[0]
a = a.strip()
a = int(a)

#Use eval() to convert to original type
#Example:
'''
>>> l = [10,20]
>>> type(l)
<class 'list'>
>>> s = str(l)
>>> print(s)
[10, 20]
>>> list(s)
['[', '1', '0', ',', ' ', '2', '0', ']']
>>> eval(s)
[10, 20]
>>> [10,20]
[10, 20]
>>> eval('10+20')
30
>>> 
'''

f1 = open(r'c:\training\log\out2.txt', 'w')
f2 = open(r'c:\training\log\out3.csv', 'w')

print(10,20,'Hello', file=f1, flush=True)
print(10,20,'Hello', sep=',',file=f2, flush=True)

f1.close()
f2.close()




