#importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("911.csv")

#printing some general info about the dataset
df.info()
print(df.head())
print(df.columns)
print(df.head())
print(df["zip"].value_counts().head())
print(df["twp"].value_counts().head())
print(len(df["title"].unique()))

#splitting the string inorder to identify the reason and storing it in another column
df["reasons"]=df["title"].apply(lambda x: x.split(":")[0])
print(df["reasons"])
print(df["reasons"].value_counts().head(3))
sns.countplot(x=df["reasons"],data=df)
plt.show()


#splitting timestamp column into hour,month,year and day of week.
df["timeStamp"]=pd.to_datetime(df["timeStamp"])
df["hour"]=df["timeStamp"].apply(lambda x:x.hour)
df["month"]=df["timeStamp"].apply(lambda x:x.month)
df["year"]=df["timeStamp"].apply(lambda x:x.year)
df["dayofweek"]=df["timeStamp"].apply(lambda x:x.dayofweek)
print(df[["hour","year","dayofweek"]])
dow={0:"mon",1:"tue",2:"wed",3:"thu",4:"fri",5:"sat",6:"sun"}
df["day"]=df["dayofweek"].map(dow)
print(df["day"])


#further visualisations
sns.countplot(x="day",data=df,hue="reasons")
plt.show()
sns.countplot(x="month",data=df,hue="reasons")
plt.show()

bymonth=df.groupby(["month"]).count()
print(bymonth)
bymonth["lng"].plot()
plt.show()
sns.lmplot(x='month',y='twp',data=bymonth.reset_index())
plt.show()

df["Date"]=df["timeStamp"].apply(lambda x:x.date())
bydate=df.groupby(["Date"]).count()
bydate["lat"].plot()
plt.tight_layout()
plt.show()

bydate_traffic=df[df["reasons"]=="Traffic"].groupby(["Date"]).count()
bydate_traffic["lat"].plot()
plt.tight_layout()
plt.show()

dow_hour=df.groupby(by=["day","hour"]).count()["reasons"].unstack()
print(dow_hour)
sns.heatmap(dow_hour,cmap="viridis")
plt.show()

dow_month=df.groupby(by=["day","month"]).count()["reasons"].unstack()
print(dow_month)
sns.heatmap(dow_month)
plt.show()