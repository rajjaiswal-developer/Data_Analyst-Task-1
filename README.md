# Data_Analyst-Task-1

# Customer Personality Analysis – Data Cleaning
This project prepares the Customer Personality Analysis dataset for analysis by performing data cleaning tasks.

## Dataset Source
- File Name: `marketing_campaign.csv`
- Source: [Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

## Columns Used
| Column Name        | Description                                   |
|--------------------|-----------------------------------------------|
| ID                 | Unique customer identifier                    |
| Year_Birth         | Customer's year of birth                      |
| Education          | Education level                               |
| Marital_Status     | Marital status (e.g., Married, Single)        |
| Income             | Yearly household income                       |
| Dt_Customer        | Customer registration date                    |
| Recency            | Days since last purchase                      |
| MntWines           | Amount spent on wine                          |
| MntMeatProducts    | Amount spent on meat products                 |
| NumWebPurchases    | Number of website purchases                   |

## Cleaning Steps
- Filled missing `Income` values with the median.
- Removed rows with unrealistic `Year_Birth`.
- Standardized `Education` and `Marital_Status`.
- Converted `Dt_Customer` to `datetime` format.
- No duplicate rows were found.

## Files
- `marketing_campaign.csv` – Raw dataset  
- `cleaned_marketing_campaign.csv` – Cleaned dataset  
- `data_cleaning_customer_personality.py` – Python cleaning script
- `Task 1 Summary-File` – Task Summary
- `README.md` – Project documentation

## Tools Used
- Python (Pandas)
- CSV file format
