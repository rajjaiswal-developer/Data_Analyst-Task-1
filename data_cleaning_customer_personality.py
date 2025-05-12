import pandas as pd
df = pd.read_csv("marketing_campaign.csv", sep=",")
df = df[['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Income', 'Dt_Customer', 'Recency', 'MntWines', 'MntMeatProducts', 'NumWebPurchases']]

# 1. Handle the Missing values

missing_income = df['Income'].isnull().sum() #Check the missing places

df['Income'].fillna(df['Income'].median(), inplace=True) # Fill missing values


# 2. Standardize Text Columns (Education, Marital_Status)

df['Education'] = df['Education'].str.strip().str.capitalize()

df['Marital_Status'] = df['Marital_Status'].str.strip().str.capitalize()

df['Marital_Status'] = df['Marital_Status'].replace({
    'Alone': 'Single',
    'Absurd': 'Other',
    'Yolo': 'Other'
})

# 3. Convert Date Column
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')

# 4. Rename columns: lowercase, replace spaces/underscores
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# 5. Remove Duplicates
df.drop_duplicates(inplace=True)

# 6. Remove future or unrealistic birth years
df = df[df['year_birth'] >= 1940]

# 7. Save the cleaned dataset
df.to_csv("cleaned_marketing_campaign.csv", index=False)


