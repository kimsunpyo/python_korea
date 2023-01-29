# 문제 1 : 머신러닝을 사용해서  300명이 반문했을 때 판매량을 예측해보세요
# pip install scikit-learn
# 머신러닝 모듈
import sklearn
# 그래프 모듈
import matplotlib.pyplot as plt
# 수학/과학 계산 모듈
import numpy as np
# 다차원 데이터 모듈
import pandas as pd
from sklearn.linear_model import LinearRegression

print(sklearn.__version__)

원본데이터 = pd.read_csv('kyobo.csv', encoding='cp949')
print(원본데이터.head())

X = 원본데이터.iloc[:,:-1].values
y = 원본데이터.iloc[:,-1].values

print(X)
print(y)


선형기계학습=LinearRegression()
선형기계학습.fit(X,y)

y_pred = 선형기계학습.predict(X)
print('예측한 y값:\n',y_pred)

print('AI예측값:',선형기계학습.predict([[300]]))

plt.scatter(X, y, color='green')     
plt.plot(X,y_pred, color='red')      
plt.title('kyobo') 
plt.xlabel('number')                  
plt.ylabel('sales rate')          
plt.show()                           