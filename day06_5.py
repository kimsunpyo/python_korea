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

'''
머신러닝(파이썬) : 데이터(정제) -> 기계학습 -> 예측결과 -> 머신러닝별 비교 후 선정 
'''
# 데이터를 가져온다
원본데이터 = pd.read_csv('sample.csv', encoding='cp949')
print(원본데이터.head())        # 잘 가져왔느지 확인    

# X(원인,) Y
X = 원본데이터.iloc[:,:-1].values
y = 원본데이터.iloc[:,-1].values
# [0,1,2]
#[[0],[1],[2]]
print(X)
print(y)

선형기계학습=LinearRegression()
# fit을 사용하면 기계학습을 한다(모델 생성)
선형기계학습.fit(X,y)

# predict 학습한 내용을 바탕으로 예측을 해
y_pred = 선형기계학습.predict(X)
print('예측한 y값:\n',y_pred)

print('AI예측값:',선형기계학습.predict([[4.5]]))
print('AI예측값:',선형기계학습.predict([[6.5],[15]]))

# 출력 print
plt.scatter(X, y, color='green')         # 원본데이터는 점으로 그려줘
plt.plot(X,y_pred, color='red')         # 예측데이터는 선으로 그려줘
plt.title('corrsion rate per Hours')        # 제목 정해줘
plt.xlabel('hours')                     # X축정해줘
plt.ylabel('corrsion rate')              # Y축정해줘
plt.show()                              # 보여줘