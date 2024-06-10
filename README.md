
# Project Title

Singapore  Resale Flat Prices Predicting



## Project workflow
1. Download the data from this link  https://beta.data.gov.sg/collections/189/view
2. Convert the data into one data frame using pandas
3.Exploratory Data Analysis (EDA) Where we will create delete and modify the converted data frame.
4. Creating a correlation heat map for the data frame to analyse the Relationship between the resale price and the other columns which help us to remove the unwanted columns for the machine learning model.
5. Splitting the data into train and testing for the model.
6. Creating the mission learning model.
7. Training that machine learning model And create a pickle file of the trained model.
8. Using the testing data to predict the model accuracy
9. With the help of the model pickle file we create a user interface  streamlit app.
10. After creating the stimuli tap we deploy the app in render so that anyone who has the url link can use the app To predict the Singapore Resale flat prices.
## Data gathering  
We used the following link https://beta.data.gov.sg/collections/189/view To get the Singapore Resale flat prices of the previous status and store it in our local system.
## Exploratory Data Analysis (EDA) 
We create a data frame and analyse the downloaded data to find the various relationship between the resale price and other columns.
1. We find the null values in the various columns and try to fill that null values using median method and dropping certain values because it does not reflect the outcome of the machine learning model.
2. We convert certain string datatype like year Into int data type, In certain cases we will divide the column into two columns and drop their previous column.
3. We create a correlation heat map to find the relationship between the columns and the resale value column. In this analysis we found that certain columns has no core relationship with the resale value column so we drop those columns from our data frame.

## Creating test and train data 
We use the following module from sklearn.model_selection import train_test_split To split the clean the data for testing and training purposes for our machine learning model. For training we allocated 70 percentage of the data and the rest of the data is used for testing the pretrained model.
## Creating the machine learning model 
After checking various models we come to the conclusion that random forest regressor is the best fit for the Singapore flat resale prediction. We use the random forest regressor method to train the model with the training data set we had. Once the model is trained he stored the trained model in a pickle file.
## Creating a streamlit application 
We use the Saved pickle Model file to predict resale flat prices we create a steamly tab where we will get the input values from the user and convert the data into required format for the model to predict the reset flat prices once the data is entered by the user the model predictor resale flat price. We use various streamlit tools like selectbox, Input method to get the data from the user.
## Deploying the app 
We create a Github repository where we  store Pickle file and our steam lit file with a text file which consists of the required modules to run the app. Once we log in in the render website we connect the render website with our Github repository by giving the access to it.
Use the web service option in the render website to connect with the Github and to deploy our app online. We connect it with the Github repository and select server region and the type of system that we want to run our app we select a system with 512MB ram Which is free for use and we deploy our app. Once the app is run by the cloud computer we will get a url link with the help of url link any anyone can use the app to predict the resale flat prices.