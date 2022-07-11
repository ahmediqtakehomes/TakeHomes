![DataRobot](logo.png)
# Predicting Loan Defaults

Predicting loan defaults is an extremely common use case for machine
learning in banking, one of DataRobot's main target industries. As a
loan officer, you are responsible for determining which loans are
going to be the most profitable and worthy of lending money to. Based
on a loan application from a potential client, you would like to
predict whether the loan will be paid back in time.

# Data

You will be working with a loan dataset
from LendingClub.com,
a US peer-to-peer lending company. Your classification target is
`is_bad`.

# Task

Partition your data into a holdout set and 5 stratified CV folds. Pick
any two machine learning algorithms from the list below, and build a
binary classification model with each of them: 
- Regularized Logistic Regression (scikit-learn)  
- Gradient Boosting Machine (scikit-learn, XGBoost or LightGBM) 
- Neural Network (Keras), with the architecture of your choice

Both of your models must make use of numeric, categorical, text, and
date features. Compute out-of-sample LogLoss and F1 scores on
cross-validation and holdout. Which one of your two models would you
recommend to deploy? Explain your decision. 

*(Advanced, optional)*: Which 3 features are the most impactful for your model?

Explain your methodology.

# Data Dictionary
|	Column Name|Type|Description|Category|
|---|---|---|---|
|`addr_state`|Categorical|Customer State|Customer
|`annual_inc`|Numeric|Annual Income|Customer
|`collections_12_mths_ex_med`|Numeric|(Credit based)|Customer
|`debt-to-income`|Numeric|Ratio of debt to income|Loan
|`delinq_2yrs`|Numeric|Any delinquency in last 2 years|Customer
|`earliest_cr_line`|Date|First credit date|Customer
|`emp_length`|Numeric|Length in current job|Customer
|`emp_title`|Text|Employee Title|Customer
|`home_ownership`|Categorical|Housing Status|Customer
|`Id`|Numeric|Sequential number|Identifier
|`initial_list_status`|Categorical|Loan status|Loan
|`inq_last_6mths`|Numeric|Number of inquiries|Customer
|`is_bad`|Numeric|1 or 0|Target
|`mths_since_last_delinq`|Numeric|Months since last delinquency|Customer
|`mths_since_last_major_derog`|Numeric|(Credit based)|Customer
|`mths_since_last_record`|Numeric|Months since last record|Customer
|`Notes`|Text|Notes taken by the administrator|Loan
|`open_acc`|Numeric|(Credit based)|Customer
|`pymnt_plan`|Categorical|Current Payment Plans|Customer
|`policy_code`|Categorical|Loan type|Loan
|`pub_rec`|Numeric|(Credit based)|Customer
|`purpose`|Text|Purpose for the loan|Loan
|`purpose_cat`|Categorical|Purpose category for the loan|Loan
|`revol_bal`|Numeric|(Credit based)|Customer
|`revol_util`|Numeric|(Credit based)|Customer
|`total_acc`|Numeric|(Credit based)|Customer
|`verification_status`|Categorical|Income Verified|Loan
|`zip_code`|Categorical|Customer zip code|Customer