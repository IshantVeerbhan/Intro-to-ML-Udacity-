#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
import sklearn
from sklearn import tree
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
c = 0
clf2 = tree.DecisionTreeClassifier()
clf2 = clf2.fit(X_train,y_train)
pred = clf2.predict(X_test)
print pred

for x in y_test:
    
    print x 
    if x == 0.0:
        c = c+1 
print clf2.score(X_test,y_test)
print c

print sklearn.metrics.precision_recall_fscore_support(y_test,pred)
