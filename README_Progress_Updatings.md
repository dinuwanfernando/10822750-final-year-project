# 10822750-final-year-project

Version 1

2024/02/07
- Started Coding on Git
- Prepared the base of the project by importing the initial library and added the dataset
- Checked the dataset and got a breakdown of it and the shape of it
- Checked for null values and initiated to handle the missing values

2024/02/09
- Continued the handling of the missing values

2024/03/04
- Handling categorical columns

2024/03/08
- Seperated features and target varialbles. Features as X and target variables as y

2024/03/10
- Evaluating the performance of different Machine Learning Models (Logistic Regression, SVC, Decision Tree Classifier, Random Forest Classifier, Gradient Boosting Classifier)
- Dividing the dataset into Test and Train sets
- Applying K-fold Cross Validation
- Started Hyperparameter tuning
- Logistic Regression, SVM and Random Forest models were selected as they had the highest accuracy out of all the 5 tested models
- ISSUE : Problem with selecting the range of the parameter for each of the model. Tried code gives an error and takes time.

2024/03/11
- ISSUE : Tried a new approach for the hyperparameter testing but failed
- Sticking with Randomized Search

2024/03/14
- ISSUE with choosing the suitable parameter for hyperparameter was solved
- Performed Randomized search for logistic regression, svc and random forest. And Random Forest is choses as it gives of the best acuracy of 80.66%

- INTERIM REPORT was submitted -

2024/04/24
- Encountered with a serious issue where the designed model heavily relied on the "Credit History" column  when predicting the output.
- Also the used dataset and the predicted values were the opposite due to a fault in feature scaling and when dividing the features and targets.

Version 2

2024/04/26
- Figured out a solution and started to reconfigure the model.

2024/04/29
- Started to code and edit the existing model.
- This is a new approach and I coded until mapping of values of each columns.

2024/04/30
- Yesterday started to code again in the existing model but to show my work and all the commits clearly, I created a new file today naming it as "loan_prediction_version2" and keeping the previous model as it is. So that I would be able to show how much I have done before I achieve the current model.
- Copied the code that was done yesterday to the new file and started working from there.
- Created new columns to the newly mapped values rather than replacing them in the same column like in the previous model.

2024/05/01
- Did the splittig of the data and then ran the model using XGBoost. I have tested many algorithms in my previous version but not XGBoost. So I will gave it a shot and analyzed whether to use XGBoost or shift to another algorith.
- Conducting setting the targets and features clearly.
- Then placed parameters accordingly.
- Then did the train, and got the prediction

2024/05/02
- Created a new dataframe with the help of joblib to check manually entered values and predict whether the Loan is Approved or Not.
- Continued testing with multiple data to check whether the version 2 model is better than version 1. And yes the version 2 model is much more better than the version 1 model.

2024/05/09
- Finally added a GUI so it is easy for the user. Now the model runs for one time and gives the user a GUI where he or she can inmput the required data and then when the desired button is pressed, a new interface is popped up with showing whether the Loan is Approved or Not along with the Credit Score.

