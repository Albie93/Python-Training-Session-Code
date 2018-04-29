#Dictionary

l = ['python', 5, ['Pune', 'Blr']]

d = {'course':'python', 'duration' : '5', 'loc' : ['Pune', 'Blr']}

e = dict(course = 'python', duration = 5, loc = ['Pune', 'Blr'])

# Print statement arguements
print(l,d,e,sep='\n', end='.') #file= , flush=
print('test')

#Dictionary is mutable
print(d['course'])

#Update/Add (if key is not there then a new key value pair is added)
d['course'] = ['java', 'python']
print(d)

d['author'] = {'fname':'Van', 'lastname': 'Rose'}
print(d)

#Remove (Use pop to remove item from dictionary)

item1 = d.pop('duration')
item2 = d.popitem()  #will randomly remove an entry
print(d)

d = {'course': ['java', 'python'], 'loc': ['Pune', 'Blr']}
print(d['course'][1])  #print python


k = d.keys()
v = d.values()
i = d.items()
print(k,v,i,sep = '\n')

