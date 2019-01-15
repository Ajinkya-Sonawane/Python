import pandas as pd
from matplotlib import pyplot as plt

def train(X,y):
    mean_X = X.mean()
    mean_y = y.mean()

    numerator = 0
    denominator = 0

    for i in range(0,len(X)):
        numerator += (X[i] - mean_X)*(y[i] - mean_y)
        denominator += (X[i] - mean_X)**2
        
    m = numerator/denominator
    b = mean_y - (m*mean_X)
    
    return m,b

def plot(X,y,predicted):
    plt.xlabel("Number of hours spent driving")
    plt.ylabel("Risk Score")
    plt.scatter(X,y)
    plt.plot(X,predicted,color="green")
    plt.savefig("Ass1.jpg")
    plt.show()


data = pd.read_csv("data.csv")
X = data.iloc[:,0]
y = data.iloc[:,1]

m,b = train(X,y)
predicted = []

for i in range(0,len(X)):
    temp = (m*X[i])+b
    predicted.append(temp)
    print(temp,y[i])

