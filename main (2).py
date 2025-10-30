#assignment using pandas series and dataframe
#create a series for your 5 fav movies with custom indexes 
import pandas as pd 
data = pd.Series(['movie1','movie2','movie3','movie4','movie5'],index=['ninnukori','dude','saiyaara','arjunreddy','geethadovindam'])
print("The series with index:\n",data)
#build a dataframe with 3 columns ;name,department,salary and access only salary column 
data1={
    'Name':['Giri','mani','arjun','vijay','vasanth'],
    'department':['cse','acccounting','ece','eee','mech'],
    'salary':[30000,40000,20000,10000,50000]
}
df=pd.DataFrame(data1)
print("The dataframe is:\n",df)
print("\n salary column:\n",df['salary'])
#load iris data and print first 10 rows 
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df.head(10))