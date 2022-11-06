import pandas as pd
import numpy as np



data=pd.read_excel(r"C:\Users\kyrie\Downloads\2 -Entrepreneurial-competency-in-university-students.xlsx")
data

data.info()
#1.	Provide the descriptive statistics for the dataset
stat = data.describe()
stat




# Drop all the raw with more than 3 missing values 
data= data[data.isnull().sum(axis=1) < 3]




# create a new variable whic contain the mean of the column 'age'
mean_age = data['Age'].mean()
print(mean_age)
# mean age equal to 19.777778 so we will replace it by 20 to avec a natural number 
mean_age = 20
data['Age'].fillna(mean_age, inplace=True)

# do the same thing for 'perseverence'
modepers = data['Perseverance'].mode()
data['Perseverance'] = np.where(data['Perseverance'].isnull(), modepers , data['Perseverance'])

# for DesireToTakeInitiative
modedesire = data['DesireToTakeInitiative'].mode()
data['DesireToTakeInitiative'] = np.where(data['DesireToTakeInitiative'].isnull(), modedesire , data['DesireToTakeInitiative'])

# for 'SelfReliance'
modeself = data['SelfReliance'].mode()
data['SelfReliance'] = np.where(data['SelfReliance'].isnull(), modeself , data['SelfReliance'])

# for GoodPhysicalHealth
modeGPH = data['GoodPhysicalHealth'].mode()
data['GoodPhysicalHealth'] = np.where(data['GoodPhysicalHealth'].isnull(), modeGPH , data['GoodPhysicalHealth'])

# for menatl disorder
modeMental = data['MentalDisorder'].mode()
data['MentalDisorder'] = np.where(data['MentalDisorder'].isnull(), modeMental , data['MentalDisorder'])


# drop the two last columns
data.drop("ReasonsForLack", axis = 1, inplace = True)
data.drop("Target-ent_competency", axis = 1, inplace = True)



# replace 'unknow' by 'yes'
data.loc[218,'City'] = 'Yes'
data.loc[137,'City'] = 'Yes'
data.loc[159,'City'] = 'Yes'




#data['KeyTraits'] = data['KeyTraits'].str.capitalize()
data['Gender'] = data['Gender'].str.capitalize()
data['KeyTraits'] = np.where(data['KeyTraits'] == "passion", "Passion" , data['KeyTraits'])

data['KeyTraits'] = np.where(data['KeyTraits'] == "Rrresilience", "Resilience" , data['KeyTraits'])

#display the unique values of each columns
for i in data.columns: 
    print(data[i].unique())

# Calculate the number of missing values.
df_missing = data.isna().sum().sort_values(ascending=False)


