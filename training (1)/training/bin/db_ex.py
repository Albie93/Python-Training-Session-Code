import sqlite3

f = open(r'C:\training\log\log_sample.txt')
data = f.readlines()
f.close()

ip = [l.split()[0] for l in data if len(l.split('.'))>0 and l.split('.')[0].isdigit()]
#print('íp =', ip)

dt = [l.split()[3][1:].split(':')[0] for l in data if len(l.split('.'))>0 and l.split('.')[0].isdigit()]
#print('dt =', dt)

#set up a connection to database first
con = sqlite3.connect('my_DB')
#con = pymysql.connect(user='',password='',database='',port='',host='')

#get cursor
cur = con.cursor()
cur.execute('create table if not exists log_data(ip varchar(100), dt varchar(100))')

cur.execute('delete from log_data')

for i,j in zip(ip,dt):
    q = "insert into log_data values('{}','{}')".format(i,j)
    cur.execute(q)

con.commit()

f2 = open(r'C:\training\log\queries.txt')
queries = f2.readlines()
f2.close()

for q in queries:
    cur.execute(q)
    r = cur.fetchall()
    print(r)

con.close()

#some functions from os module
import os

os_dir = r'C:\training'
r = os.walk(os_dir)
print(r)

for r,s,f in os.walk(os_dir):
    for x in f:
        print(r+'\\'+x)
    




