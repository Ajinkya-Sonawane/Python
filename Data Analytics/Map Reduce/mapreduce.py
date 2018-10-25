"""
    Author : Ajinkya Sonawane
"""
import pandas as pd

data = pd.read_csv('ratings_small.csv')
#print(data)
data = data.iloc[:1000,:]

def find(movieId):
    global data
    temp = []
    for index,row in data.iterrows():
        if row['movieId'] == movieId:
            temp.append(row['rating'])
    return temp

def process():
    unique_movei_ids = set(data['movieId'])
    mapped_values = {}
    reduced_values = {}
    
    #Map the ratings with same movie id
    for i in list(unique_movei_ids):
        mapped_values[i] = find(i)
        
    #Reduce the mapped values by taking the average of the ratings
    for key,value in mapped_values.items():
        reduced_values[key] = sum(value)/len(value)
        print(key,':',mapped_values[key],'-->',reduced_values[key])

process()
