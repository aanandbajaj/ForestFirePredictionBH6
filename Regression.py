# -*- coding: utf-8 -*-
"""Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TZXtT2VLRyO4nUaT5lXZJjfqWKP8IKIY
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd  
import numpy as np  
# import matplotlib.pyplot as plt
# import seaborn as seabornInstance
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn import metrics
# %matplotlib inline
import statsmodels.api as sm
from scipy import stats


from pandas import HDFStore


url = 'https://raw.githubusercontent.com/aanandbajaj/ForestFirePredictionBH6/master/Forest%20Fire%20Data.csv'
data = pd.read_csv(url)
df = pd.DataFrame(data)


X = data[['temp', 'RH', 'wind', 'rain']].values
y = data['area0'].values

#sci-kit method, commented out
#plt.figure(figsize=(15,10))
#plt.tight_layout()
#seabornInstance.distplot(data['area'])

#80% of the data will be training, 20% of the data will be test
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#regressor = LinearRegression()  

#regressor.fit(X_train, y_train)

#df2 = pd.DataFrame(regressor.coef_, columns=['Coefficient'],index=[ 'temp', 'RH', 'wind', 'rain'])
#df2

X = sm.add_constant(X)
est = sm.OLS(y, X).fit()
est.summary()

print(est.params)
#print(est.rsquared)
print(str(est.summary()))

# regression coefficients
tempSlope = est.params[1]
relHumiditySlope = est.params[2]
windSlope = est.params[3]
rainSlope = est.params[4]
yIntercept = est.params[0]

# regression coefficients confidence intervals (10%, two-tailed)
# degrees of freedom is n - 2
# n = 515
# n - 2 = 513

print(est.tvalues)
standardErrors = est.bse
tValues = est.tvalues

# from critical t - table
tCrit = 1.283

# index 0 is min
# index 1 is max
# can use normal distribution to generate 
CI_yIntercept = [yIntercept - tCrit*standardErrors[0],yIntercept + tCrit*standardErrors[0]]
CI_temp = [tempSlope - tCrit*standardErrors[1],tempSlope + tCrit*standardErrors[1]]
CI_relHumidity = [relHumiditySlope - tCrit*standardErrors[2],relHumiditySlope + tCrit*standardErrors[2]]
CI_wind = [windSlope - tCrit*standardErrors[3],windSlope + tCrit*standardErrors[3]]
CI_rain = [rainSlope - tCrit*standardErrors[4],rainSlope + tCrit*standardErrors[4]]

def predictBurnedArea(temp,relHumidity,wind,rain):
  y = temp*tempSlope + relHumidity*relHumiditySlope + wind*windSlope + rain*rainSlope + yIntercept
  return y