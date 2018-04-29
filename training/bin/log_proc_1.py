
f = open(r'c:\training\log\log_sample.txt')
data = f.readlines()



f.close()
#print(data)

out1 = open(r'c:\training\log\report1.txt','w')
out2 = open(r'c:\training\log\report2.csv','w')

for each_line in data:
    sp1 = each_line.split('.')
    if len(sp1)>0 and sp1[0].isdigit():
        sp2 = each_line.split()
        print(sp2)
        ip = sp2[0]
        print(ip)
        dt = sp2[3]
        dt = dt[1:]
        dt = dt.split(':')
        dt = dt[0]
        print(dt)
        if sp2[6].find('pics') == -1:
            im = 'No Image'
        else:
            im = sp2[6].split('/')
            im = im[-1]
            print(im)
        ws = sp2[10].split('//')
        ws = ws[1].split('/')
        ws = ws[0]
        print(ws)
        print(ip,dt,im,ws,file=out1)
        print(ip,dt,im,ws,sep=',',file=out2)

out1.close()
out2.close()

#List comprehensions

l = [i for i in range(10)]
m = [j for j in range(10) if j%2 == 0]

ip = [l.split()[0] for l in data if len(l.split('.'))>0 and l.split('.')[0].isdigit()]
print('íp =', ip)

dt = [l.split()[3][1:].split(':')[0] for l in data if len(l.split('.'))>0 and l.split('.')[0].isdigit()]
print('dt =', dt)

pic = [l.split()[6].split('/')[-1]  if l.split()[6].find('pics')!=-1 else 'No Image' for l in data if len(l.split('.'))>0 and l.split('.')[0].isdigit()] 
print('pic =', pic)

out1 = open(r'c:\training\log\report1.txt','w')

for i,j,k in zip(ip,dt,im):
    print(i,j,k,file=out1)

out1.close()
