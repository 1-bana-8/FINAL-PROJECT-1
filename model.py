

import pandas as pd
set=pd.read_csv("Albury.csv")
j=pd.get_dummies(set["WindGustDir"])
i=pd.get_dummies(set["WindDir9am"])
h=pd.get_dummies(set["WindDir3pm"])
e=pd.get_dummies(set["RainTomorrow"],drop_first=True)
set=pd.concat([e,h,i,j],axis=1)
set.drop(["Date","Location","Cloud9am","Cloud3pm","Evaporation","Sunshine","WindGustDir","WindDir9am","WindDir3pm","RainToday","RainTomorrow","Cloud9am","Cloud3pm"],axis=1,inplace=True)
set.dropna(inplace=True)
m=set.drop("Yes",axis=1)
n=set["Yes"]
from sklearn.preprocessing import LabelEncoder
l_x=LabelEncoder()
n=l_x.fit_transform(n)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(m,n,test_size=0.2)
from sklearn.linear_model import LogisticRegression
c = LogisticRegression()
c.fit(x_train,y_train)
p=c.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,p))

