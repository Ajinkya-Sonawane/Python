import pandas as pd
import math
from statistics import mean

class NB:
    def __init__(self):
        self.prob_1 = 0
        self.prob_0 = 0
        self.labels = ['very low','low','medium','high','very high']
        self.data = []

    def replace(self,avg,i,data):
        """Function to replace missing values with the given mean value """
        for j in range(len(data)):
            if data.iloc[j,i] == 0:
                data.iloc[j,i] = avg
        return data

    def discretize(self,data,labels):
        """ Function to discretize or categorize the input into the given labels"""
        temp = []
        for i in list(data.columns)[:-1]:
            data[i] = pd.cut(data[i],bins=len(labels),labels=labels)
        return data

    def count(self,data,col,source,target):
        count = 0
        d_col = list(data[col])
        for i in range(0,len(data)):
            #Count the number of rows where with given category the target is present
            if d_col[i] == source and data.iloc[i,-1] == target:
                count += 1
        return count

    def probability(self,data,col,source,target):
        x = self.count(data,col,source,target)
        y = self.count(data,'Outcome',target,target)
        return x/y

    def train(self,data):
        temp = []
        for i in list(data.columns)[:-1]:
            #Dictionary to store the probabilities of various categories with different class
            d = {i:{1:{},0:{}}}        
            for j in self.labels:
                x = self.probability(data,i,j,1)
                y = self.probability(data,i,j,0)
                d[i][1][j] = x
                d[i][0][j] = y
            temp.append(d)
        return temp

    def test(self,data,temp):
       results = []
       for i in range(0,len(data)):
           op_1 = 1     #Probability of class 1 for given features
           op_0 = 1     #Probability of class 0 for given features
           c = 0    #To iterate through different features
           for j in data.columns:
               #Using Baye's formula
               op_1 *= temp[c][j][1][data.iloc[i,c]]
               op_0 *= temp[c][j][0][data.iloc[i,c]]
               c += 1
           #Whichever probability is greate output result as that class
           if op_1 > op_0:
               results.append(1)
           else:
               results.append(0)
               
       return results

    def process(self,train_per):

        #Read the input file
        self.data = pd.read_csv("diabetes.csv")
        
        # Traverse respective columns and replace missing values with the mean
        for i in range(1,len(list(self.data.columns))-1):
            avg = mean(self.data.iloc[:,i])
            self.data = self.replace(math.floor(avg),i,self.data)

        #Discretize the data
        self.data = self.discretize(self.data,self.labels)

        #Calculate probability of output being 1 or 0
        self.prob_1 = self.probability(self.data,'Outcome',1,1)
        self.prob_0 = self.probability(self.data,'Outcome',0,0)

        # Split dataset into training and test data
        train_len = len(self.data)*train_per/100
        train_len = math.floor(train_len)
        train_data = self.data.iloc[:train_len,:]
        test_data = self.data.iloc[train_len+1:,:]

        #Train the model
        temp = self.train(train_data)

        #Test the model
        results = self.test(test_data.iloc[:,:-1],temp)

        #Calculate confusion matrix
        """
        TP : Actual Yes Predicted Yes
        TN : Actual No  Predicted  No

        FP : Actual No  Predicted Yes
        FN : Actual Yes Predicted   No
        """
        tp,tn = 0,0
        fp,fn = 0,0
        for i in range(0,len(results)):
            if test_data.iloc[i,-1] == 1:
                if results[i] == test_data.iloc[i,-1]:
                    tp+=1
                else:
                    fn+=1
            else:
                if results[i] == test_data.iloc[i,-1]:
                    tn+=1
                else:
                    fp+=1

        accuracy = (tp+tn)/(tp+tn+fp+fn)
        misclassification = (fp+fn)/(tp+tn+fp+fn)
        print('\n----------------------------------------------')
        print('\nConfusion Matrix with Training : '+str(train_per)+' Test : '+str(100-train_per))
        print('\n\t\tActual Yes\tActual No')
        print('Predicted Yes\tTP='+str(tp)+'\t\tFP='+str(fp))
        print('Predicted No \tFN='+str(fn)+'\t\tTN='+str(tn))
        print('\nAccuracy : ',(accuracy*100))
        print('Misclassification rate : ',(misclassification*100))

n = NB()
n.process(70)
n.process(30)
n.process(80)
n.process(20)
