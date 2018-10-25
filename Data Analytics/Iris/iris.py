import pandas as pd
import matplotlib.pyplot as plt

class Iris:
    def  __init__(self):
        self.data = []
    
    def process(self):
        self.data = pd.read_csv('data.csv')

        #Display number of features
        print('Total Features : ',len(self.data.columns))
        print('Features : ',list(self.data.columns),"\n")
        for i in self.data.columns:
            print(i,':',self.data[i].dtype)

        for i in self.data.columns:
            if i != 'class':
                print('\nFeature : ',i)
                print('Min : ',self.data[i].min())
                print('Max : ',self.data[i].max())
                print('Median : ',self.data[i].median())
                print('Variance : ',self.data[i].var())
                print('Standard Deviation : ',self.data[i].std())
                print('Range : ',self.data[i].min(),' : ',self.data[i].max())

        #Plot Histogram
        for i in self.data.columns:
            plt.hist(x=self.data[i],label=i)
            plt.show()

        #Plot boxplot    
        boxplot = self.data.boxplot(by='class')
        plt.show()
                    
i = Iris()
i.process()
i.data.boxplot(by='class')
