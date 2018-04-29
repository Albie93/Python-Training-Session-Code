import re

f = open(r'C:\training\log\log_sample.txt')
data = f.readlines()
f.close()

for line in data:
    m = re.match('(\d{3}\.\d{1,3}.\d{1,3}\.[0-9]{3}).*(\d{2}/[A-Za-z]{3}/\d{4}).*pics/(\w+\.\w+).*http://(\w+\.\w+\.\w+).*', line)
    #print(m)
    if m != None:
        ip = m.group(1)
        dt = m.group(2)
        im = m.group(3)
        ws = m.group(4)
        print(ip)
        print(dt)
        print(im)
        print(ws)

print(__name__)

#In regular expression w is word character which is same as [A-Za-z0-9_]
