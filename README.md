• Overview of insights from EDA
The dataset is generally clean, with only minor missing values in features such as age and previous_contact_days, and several non-informative ID-like columns were removed. The target variable, subscription_status_encoded, is highly imbalanced, with far fewer positive subscriptions, which significantly affects model performance and motivated the use of techniques like oversampling and class weighting. From the exploratory analysis, customers with higher education levels, certain job types, and those contacted via cellular tend to show higher subscription rates, while features such as housing loan, personal loan, and credit default show little relationship with the target. Numerical features like age, balance, campaign, and pdays are skewed with expected outliers, though correlations between numerical variables remain weak. A key insight from the previous campaign data shows that customers previously contacted are more likely to subscribe, which led to creating the previous_contact_flag, one of the stronger engineered features. Overall, the EDA highlights class imbalance as the main challenge and identifies meaningful predictors that guide model training.

• Explanation of choice of models
We selected XGBoost, Random Forest, and MLPClassifier because they represent three different modelling families — boosting, bagging, and neural networks. This allows us to compare how different algorithms handle our imbalanced and mixed-type bank marketing dataset.
XGBoost: high performance, strong with imbalance
Random Forest: robust, interpretable, reliable baseline
MLPClassifier: captures deeper non-linear interactions

• How to run pipeline(s)
docker build -t banking-project
docker run -v ${PWD}/data:/app/data banking-project

• Who does what
Chancelier did the startup of the EDA+data cleaning and setting up of the github repositories, Marcus did the fine tuning of EDA, Docker and the models and lastly Gregory completed the Kedro, the docker and fine-tuning mlp models of the project
