# Crop-Damage-prediction-end-to-end

Link to the site: http://3.138.37.88:5000/

Aim: Trying to replicate complete end to end Machine Learning deployment.

Problem statement: You need to determine the outcome of the harvest season, i.e. whether the crop would be healthy (alive), damaged by pesticides or damaged by other reasons.
                   https://datahack.analyticsvidhya.com/contest/janatahack-machine-learning-in-agriculture/#MySubmissions

Cloud and tools used:
1. AWS RDS(PostgreSQL)
2. Jupyter notebook
3. Flask
4. HTML/CSS
5. Docker
6. AWS EC2

Steps followed:

  1. AWS RDA(PostgreSQL) was created to store the data with more than 80k+ rows.
  
  2. These data were extracted from RDS and was used for analysis and Modeling.
  
  3. A complete analysis of data was done with help of graphs.
  
  4. Based on EDA feature engineering was done.
  
  5. Later modeling was done with algorithms like Logistic regression, RandomForestClassifier, LBGMClassifier, and CatBoostClassifier.
  
  6. Stratified cross-validation was done and then SMOTE to balance our target variable.
  
  7. Got the best accuracy of 83.82% from LBGMClassifier with good precision.
  
  8. Saved the mode as Pickle_LGBM_Model.pkl file.
  
  9. Developed a flask model where this pkl file loaded.
  
  10. Created an AWS EC2 instance uploaded the required file using Docker.
