1st step: Download the Git Repository from the my Git - https://github.com/dinuwanfernando/10822750-final-year-project.git 

2nd step: Locate the downloaded repository and extract it. Then open command prompt and navigate to the directory containing the files.

3rd step:	There are several things that needed to be installed before being able to run this model. 
    I.	Install Python if you have not installed already on your device.
   II.	Install Jupyter Notebook by using the command pip install notebook in your Command Prompt.
4th step:	Now that you have the base setup in your device to run the model, type the command jupyter-notebook or jupyter notebook in the command prompt to fire up Jupyter Notebook and make sure that you are in the directory containing the files of the downloaded repository.

5th step: Once the Jupyter Notebook is opened through your local host, now double click on the file loan_prediction_version2.ipynb.

6th step: Now once you open then file, then select Run and then select Run All Cells to run the whole model. This will take roughly about 10 seconds or can be even less based on the specifications of the users device.

7th step: After the whole model has completed running, a GUI will pop up with a title as Loan Status Predictor.

8th step: The user will be able to see multiple labels and multiple entry fields and a button at the end.

9th step: The user can now enter values. Important Note – The loan amount is in hundred thousand.
Lets input a sample set of data;

    Applicant Income: 1500 ---- this is the monthly income

    Coapplicant Income: 200 ---- this is the monthly income of the co applicant

    Loan Amount: 100 ----- this equals to 100,000
    Loan Amount Term: 60 ---- as this is a model for mortgage loans, the terms are 5 years based. 60 = to 5 years, 120 = 10 years, 180 = 15 years and 360 = 30 years.

    Credit History: Good ---- further this model can be improved by giving the crib credit score data to determine the credit history quality instead of Good or Bad if the data is available to train the model with such data.

    Married: Yes 

    Education: Graduated

    Self Employed: Yes

    Property Area1: Semiurban

    Dependents: 1

10th step: Once the desired values are entered, the user can simply click “Check Loan Status” button and the GUI will prompt another window stating whether the Loan is Approved or Not Approved along with a custom credit score


