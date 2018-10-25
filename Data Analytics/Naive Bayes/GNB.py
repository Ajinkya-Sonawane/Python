from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import confusion_matrix

data = pd.read_csv('diabetes.csv')
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


clf = GaussianNB()
clf.fit(X_train,y_train)

print(clf.predict(X_test))
tn, fp, fn, tp = confusion_matrix(clf.predict(X_test),y_test).ravel()
print(tn, fp, fn, tp)
