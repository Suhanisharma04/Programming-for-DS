#using list
import pandas as pd

product_data = [['e-book', 2000], ['plants', 6000], ['Pencil', 3000]]
indexes= [1,2,3]
columns_name= ['Product', 'Unit_Sold']
product_df= pd.DataFrame(data= product_data, index=indexes, columns=columns_name)
print(product_df)

#using dictionaries

product_data = {'product':['e-book','plants','Pencil'], 'unit_sold':[2000, 6000, 3000]}
product_df = pd.DataFrame(data=product_data)
print(product_df)

#using numpy array
import numpy as np

products = np.array([['', 'product', 'unit_sold'], [1, 'E-book', 2000], [2, 'Plants', 6000], [3, 'Pencil', 3000]])
product_pf = pd.DataFrame(data=products[1:,1:], index=products[1:,0], columns= products[0,1:])
print(product_pf)

#reading a file
import pandas as pd

df= pd.read_csv('C:/Users/c7371613/Downloads/dirtydata.csv')
print(df)

#Information about the data
print(df.info())
print(df.isna().sum())
print(df.duplicated())

#Remove rows
df = pd.read_csv('C:/Users/c7371613/Downloads/dirtydata.csv')
new_df = df.dropna()
print(new_df.to_string())

#Replace empty values
df= pd.read_csv('C:/Users/c7371613/Downloads/dirtydata.csv')
df_new = df.fillna(130)
print(df_new.to_string())  #Replaces values for all empty columns

#Replacing only for specified columns
df= pd.read_csv('C:/Users/c7371613/Downloads/dirtydata.csv')
df_cal = df["Calories"].fillna(130)
print(df_cal.to_string())

#replace using mean
df =pd.read_csv('C:/Users/c7371613/Downloads/dirtydata.csv')
x = df["Calories"].mean()
df["Calories"] = df["Calories"].fillna(x)
print('df after fill na with mean\n', df)

#replace using median
df =pd.read_csv('C:/Users/c7371613/Downloads/dirtydata.csv')
x= df["Calories"].median()
print('x', x)
df["Calories"] = df["Calories"].fillna(x)
print('df after fill na with median\n', df)

#replace using mode
x= df["Calories"].mode()
df["Calories"] = df["Calories"].fillna(x)
print('df after fill na with mode\n', df)