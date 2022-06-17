import numpy as np
import os
import pandas as pd
from pandas.io.parsers import read_csv
import datetime as dt
from plotnine import *
from matplotlib import pyplot as plt
import statsmodels.formula.api as smf
from sklearn.metrics import mean_squared_error
import seaborn as sns; sns.set()

df = read_csv('mtcars.csv')
print(df.shape)
print(df.head(5))
print(df.describe())

x = 'wt'
y = 'mpg'

# 자동차의 무게(wt)와 연비(mpg)의 산점도 그래프
plt.scatter(df.wt, df.mpg)
pt1 = (1.5,30*-5.30 + 37.10)
pt2 = (5.5,9*-5.30 + 37.10)
plt.plot( [pt1[1],pt2[1]],[pt1[0], pt2[0]])
plt.xlabel('weight')
plt.ylabel('miles per gallon')
plt.grid()
plt.savefig('wt-mpg.png')
#ax = sns.lmplot(x="wt", y="mpg", data = df)
plt.show()


#(최대값, 최소값, 간격)
slopeList = np.arange(-10, 10, 0.1)
interceptList = np.arange(30, 40, 0.1)

ref = df['mpg']

dataL1 = pd.DataFrame()
for i, slope in enumerate(slopeList):
    for j, intercept in enumerate(interceptList):
        # 임의의 모수 및 무게를 이용하여 예측 mpg 계산
        prd = (df['wt'] * slope) + intercept
        # 예측 결과 및 실측 결과를 비교하여 RMSE 계산
        rmse = np.sqrt(mean_squared_error(ref, prd))

        # 값 저장을 위한 딕션너리
        dict = {
            'slope' : [slope]
            , 'intercept' : [intercept]
            , 'rmse' : [rmse]
        }

        # 임의의 모수 및 RMSE 구하기
        dataL1 = pd.concat([dataL1, pd.DataFrame.from_dict(dict)], axis=0, ignore_index=True)

# RMSE가 최소가 되는 인덱스
idx = dataL1.idxmin()['rmse']

# 산점도 시각화
mainTitle = '{}'.format('시뮬레이션에 따른 RMSE 결과')
saveImg = './{}'.format(mainTitle)

plt.plot(dataL1['rmse'], 'o')
plt.xlabel('index')
plt.ylabel('RMSE')
plt.savefig(saveImg, dpi=600, bbox_inches='tight', transparent=True)
plt.show()
plt.close()
