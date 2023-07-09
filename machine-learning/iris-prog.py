#Importing all the necessary modules and libraries
import sklearn
#Importing the iris dataset from scikit learn
from sklearn.datasets import load_iris
#Importing accuracy_score to show us the accuracy of our predictions
from sklearn.metrics import accuracy_score
#Importing shuffle function to shuffle the dataset to make sure our model sees different types of flowers in approximately equal numbers
from sklearn.utils import shuffle
iris = load_iris()
import pandas as pd
#Loading the dataset into a pandas dataframe
data = pd.DataFrame(data=iris.data,columns=iris.feature_names)
#SHuffling the data and the targets
shuffled_data,shuffled_target=shuffle(data,iris.target)

from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
#Splitting the data into training and test data. 20% of the data is used for testing purpose
X_train,X_test,y_train,y_test = train_test_split(shuffled_data,shuffled_target,test_size=0.2)
#Fitting a logistic regression model to our data and doing 5-fold cross validation
log_reg= linear_model.LogisticRegression().fit(X_train,y_train)

y_predicted = log_reg.predict(X_test)
scores= cross_val_score(log_reg,X_test,y_test,cv=5)
#Reporting the accuracy of our prediction by comparing the actual and predicted y values
print("Accuracy score:",scores.mean())