#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



#import dataset
dataset = pd.read_csv('Data.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values


#take care of missing data
from sklearn.preprocessing import Imputer
imputer  = Imputer(missing_values='NaN',strategy='mean',axis = 0)
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3]) #impute the missing values to the mean

#Encode categorial data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[:,0] = labelencoder_x.fit_transform(x[:,0])

onehotencoder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#Splitting dataset into training and test set
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test =  train_test_split(x,y,test_size = 0.2,random_state = 0)

