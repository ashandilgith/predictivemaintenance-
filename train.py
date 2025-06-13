#Import the libraries 

import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error 
import joblib
from huggingface_hub import HfApi, HfFolder, create_repo 
from sklearn.metrics import r2_score


#Create a train model function 

def train_model():


#Load the data 

    df = pd.read_csv("data/processed_data.csv")

#Split the data into X and Y (dependent variable and parameters)

    features = ['time_in_cycles','setting_1', 'setting_2'] + [f's_{i}' for i in range (1,22) if f's_{i}' in df.columns]

    target = 'RUL'

    X = df[features]
    y = df[target]

#Perform the train test split 

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=42)

 #Load the model - in this case from Scikit-Learn 

    model = LinearRegression()


#Train the model on the training data 

    model.fit(X_train, y_train)

    #evaluate the model 

#Make your first prediction 

    y_pred = model.predict(X_test)


#Calculate the accuracy of the model 

    r2 = r2_score(y_test, y_pred)

    print(f'R_squared score is {r2}')

#Save the model 

    joblib.dump(model, 'model.joblib')

#Ensure the function is called with the script 

if __name__ == '__main__':
    train_model()
