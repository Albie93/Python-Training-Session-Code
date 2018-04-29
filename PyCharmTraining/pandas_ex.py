import pandas as pd
s = pd.Series([1,2,3,4,5])
print(s)
s = pd.Series([1,2,3,4,5], index=[100,200,300,400,500])
print(s)
print(s[100])
#print(s[3])
print(s[[100,300]])
print(s.axes)
print(s.empty)
print(s.size)
print("Next")
print(s.head(2))
print(s.tail(2))

#Dataframe is used for 2D : rows and cloumns

df = pd.DataFrame()
L = [10,20,30,40,50]
df = pd.DataFrame(L)
print(df)
L = [['A',10],['B',20],['C',30]]
df = pd.DataFrame(L)
print(df)
df = pd.DataFrame(L, index=['a','b','c'],columns=['Name', 'Increment'])
print(df)
df.to_csv('Sample.csv')
print(df.T)
print(df.axes)
print(df.head(2))
print(df.tail(1))
print(df.size)
print(df.empty)
print(df.describe())

#Panel : used for 3 dimensional data mapping

df = pd.Panel()

d = {'item1':pd.DataFrame(L),
     'item1': pd.DataFrame(L)}
df = pd.Panel(d)
print(df)
