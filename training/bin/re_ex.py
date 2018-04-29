import re

f = open(r'C:\training\log\log_sample.txt')
data = f.readlines()
f.close()

for line in data:
    m = re.match('(\d{3}\.\d{1,3}.\d{1,3}\.[0-9]{3}).*', line)
    #print(m)
    if m != None:
        ip = m.group(1)
        print(ip)
        
