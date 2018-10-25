# Importing the required packages 
import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 

import graphviz

# Function importing Dataset 
def importdata(): 
	balance_data = pd.read_csv('capitalshare.csv') 
	balance_data = balance_data[['Duration','Start station number','End station number','Member type']]
	#print(balance_data)
	# Printing the dataswet shape 
	print ("Dataset Lenght: ", len(balance_data)) 
	print ("Dataset Shape: ", balance_data.shape) 
	
	# Printing the dataset obseravtions 
	print ("Dataset: ",balance_data.head()) 
	return balance_data 

# Function to split the dataset 
def splitdataset(balance_data): 

	# Seperating the target variable 
	X = balance_data.values[:, :-1] 
	Y = balance_data.values[:, -1] 

	# Spliting the dataset into train and test 
	X_train, X_test, y_train, y_test = train_test_split( 
	X, Y, test_size = 0.3, random_state = 100) 
	
	return X, Y, X_train, X_test, y_train, y_test 

#Function to visualize tree
def visualize_tree(data,clf,clf_name):
	features = data.columns
	features = features[:-1]
	class_names = list(set(data.iloc[:,-1]))
	dot_data = tree.export_graphviz(clf, out_file=None,  feature_names=features,class_names=class_names,  filled=True, rounded=True, special_characters=True)
	graph = graphviz.Source(dot_data)
	graph.render('dtree_render_'+clf_name,view=True)

# Function to perform training with giniIndex. 
def train_using_gini(X_train, X_test, y_train,data): 

	# Creating the classifier object 
	clf_gini = DecisionTreeClassifier(criterion = "gini", 
			random_state = 100,max_depth=3, min_samples_leaf=5)
        # Performing training 
	clf_gini.fit(X_train, y_train)
	visualize_tree(data,clf_gini,'gini')
	print('\nFeature Importance : ',clf_gini.feature_importances_)
	return  clf_gini 
	
# Function to perform training with entropy. 
def tarin_using_entropy(X_train, X_test, y_train,data): 

	# Decision tree with entropy 
	clf_entropy = DecisionTreeClassifier( 
			criterion = "entropy", random_state = 100, 
			max_depth = 3, min_samples_leaf = 5) 

	# Performing training 
	clf_entropy.fit(X_train, y_train)
	visualize_tree(data,clf_entropy,'entropy')
	print('\nFeature Importance : ',clf_entropy.feature_importances_)
	return clf_entropy


# Function to make predictions 
def prediction(X_test, clf_object): 

	# Predicton on test with giniIndex 
	y_pred = clf_object.predict(X_test) 
	print("Predicted values:") 
	print(y_pred) 
	return y_pred 
	
# Function to calculate accuracy 
def cal_accuracy(y_test, y_pred): 
	
	print("Confusion Matrix: ", 
		confusion_matrix(y_test, y_pred)) 
	
	print ("Accuracy : ", 
	accuracy_score(y_test,y_pred)*100) 
	
	print("Report : ", 
	classification_report(y_test, y_pred)) 

# Driver code   
def main(): 
	
	# Building Phase 
	data = importdata() 
	X, Y, X_train, X_test, y_train, y_test = splitdataset(data) 
	clf_gini = train_using_gini(X_train, X_test, y_train,data) 
	clf_entropy = tarin_using_entropy(X_train, X_test, y_train,data) 
	
	# Operational Phase 
	print("Results Using Gini Index:") 
	
	# Prediction using gini 
	y_pred_gini = prediction(X_test, clf_gini) 
	cal_accuracy(y_test, y_pred_gini) 
	
	print("Results Using Entropy:") 
	# Prediction using entropy 
	y_pred_entropy = prediction(X_test, clf_entropy) 
	cal_accuracy(y_test, y_pred_entropy) 
	
	
# Calling main function 
if __name__=="__main__": 
	main() 
