#Importing the necessary libraries
import sklearn
import pandas as pd
#Importing the boston housing data to perform regression
from sklearn.datasets import load_boston
boston=load_boston()
#Loading the data into a dataframe
boston_df = pd.DataFrame(data=boston.data,columns=boston.feature_names)

from sklearn.model_selection import train_test_split,cross_val_score
#Separating the variables into features and the required output variable
predictors= boston_df.iloc[:,:13]
target=boston_df.iloc[:,12:13]

print(target)
#SPlitting the data into training and testing data by using existing function
X_train,X_test,y_train,y_test = train_test_split(predictors,target,test_size=0.2)
#Importing linear regression function from sklearn and fitting it to the training data
from sklearn import linear_model
reg = linear_model.LinearRegression().fit(X_train,y_train)
#Performing 5-fold cross validation and then testing the model on test data
scores= cross_val_score(reg,X_test,y_test,cv=5)
#Checking the accuracy of our prediction
print('Accuracy of prediction:',scores.mean())