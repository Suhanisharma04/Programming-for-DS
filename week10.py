import numpy as np
import pandas as pd
import gradio as gr
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('diabetes.csv')
print(data.head())
print(data.columns)

x= data.drop(['Outcome'], axis=1)
y = data['Outcome']

#split data
x_train,x_test,y_train,y_test= train_test_split(x,y)

#scale data
scaler= StandardScaler()
x_train_scaled= scaler.fit_transform(x_train)
x_test_scaled= scaler.fit_transform(x_test)

#instatiate model
model=MLPClassifier(max_iter=1000,alpha=1)
model.fit(x_train,y_train)
print("Model Accuracy on Training Set:", model.score(x_train,y_train))
print("Model Accuracy on Test Set:", model.score(x_test,y_test))

#getting columns
print(data.columns)

#creating function for gradio
def diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    x=np.array([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    prediction=model.predict(x.reshape(1,-1))
    return prediction

outputs= gr.Textbox()
app=gr.Interface(fn=diabetes,
inputs= ['number', 'number', 'number', 'number', 'number', 'number', 'number', 'number'],
outputs= outputs, description= "This is a diabetes model")

app.launch(share=True)







