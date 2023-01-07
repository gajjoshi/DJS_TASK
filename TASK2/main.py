import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

train_path = 'train.csv'
test_path = 'test.csv'
train_df=pd.read_csv(train_path)
test_df=pd.read_csv(test_path)

print(train_df.head(100))
print(train_df.tail(20))





for x in train_df.columns:
  print(x)



print(len(train_df))
print(len(train_df.columns))
print(train_df.info())
print(train_df.describe())
dict1=dict()
l1=[]
for y in train_df.columns:
    a=str(y)
    #print(train_df[a].unique().tolist())
    dict1[a]=train_df[a].unique().tolist()
for k, v in dict1.items():
    print(k, v)

titlelist=[]
for name in train_df.Name :
  title_search = re.search('(\w+)\.', name) #the first argument is a pattern that we are looking for
  #print("result:", title_search) #this is the result we get after looking for the pattern
  if title_search:
    title = title_search.group(1) #extracting the pattern found by regular expression (title here)
    titlelist.append(title)

train_df["Title"] = titlelist

#l2=[]
tl_unique = list(set(titlelist))
print(tl_unique)

uniquetitle = list(train_df['Title'].unique())
print(uniquetitle)

name = []
total = float(train_df["Survived"].count())
survive= {}
for i in uniquetitle:
  survived = float(train_df.loc[(train_df['Title'] == i) & (train_df['Survived'] == 1), 'Survived'].sum())
  survived = float(survived / total)
  survive[i] = survived
SR_df = pd.DataFrame(survive.items(), columns=['Title', 'Survival Rate'])
print(SR_df)
l3=SR_df['Title'].tolist()
l2=SR_df['Survival Rate'].tolist()


plt.bar(l3, l2, color='maroon',
        width=0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()
plt.close()
sur=0
dead=0
for x in train_df['Survived']:
  print(x)
  if int(x)==1:
    sur=sur+1
  elif int(x)==0:
    dead=dead+1

pie_list0=[sur,dead]



plt.pie(pie_list0, labels = ['survived','dead'])
plt.show()
plt.close()



pie_list1=[int(train_df.loc[(train_df['Sex']=='male') & (train_df['Survived']==1),'Survived'].sum()),int(len(train_df)-int(train_df.loc[(train_df['Sex']=='male') & (train_df['Survived']==1),'Survived'].sum()))]
plt.pie(pie_list1, labels = ['survived','dead'])
plt.show()
plt.close()

pie_list2=[int(train_df.loc[(train_df['Sex']=='female') & (train_df['Survived']==1),'Survived'].sum()),int(len(train_df)-int(train_df.loc[(train_df['Sex']=='female') & (train_df['Survived']==1),'Survived'].sum()))]
plt.pie(pie_list2, labels = ['survived','dead'])
plt.show()
plt.close()




train_df.drop(['PassengerId','Ticket','Name'],axis=1,inplace=True)
print(train_df)
l1=[]
d=dict()
for y in train_df.columns:
  count=0
  for x in train_df[y]:
    if str(x) == 'nan':
      count=count+1
  count=(count*100)/len(train_df)
  d[y]=count
  if count>50:
    train_df.drop([y],axis=1,inplace=True)

for k, v in d.items():
    print(k, v)

print(train_df)
l1.clear()
l2.clear()
l3.clear()
l1=train_df['Parch'].tolist()
l2=train_df['SibSp'].tolist()
for i in range(0,len(l1)):
  try:
    l3.append(int(l1[i]) + int(l2[i]))
  except:
    pass

for x in l3:
  print(x)

train_df.drop(['Parch','SibSp'],axis=1,inplace=True)
train_df['Family_members']=l3

print(train_df)

















