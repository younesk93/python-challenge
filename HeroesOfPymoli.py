# Dependencies and Setup

import pandas as pd
import numpy 
import os

# Find path

Currentpath = os.getcwd()
Currentpath

# '/Users/Younes/Desktop/Useful-Repository-master/HeroesOfPymoli'

# Read CVS file

df = pd.read_csv("Purchase_Data.csv") 
df.head()

# Display the columns

df.columns

# Index(['Purchase ID', 'SN', 'Age', 'Gender', 'Item ID', 'Item Name', 'Price'], dtype='object')

# Display the total number of players

df_Count = len(df["SN"].unique())
Number_Players = pd.DataFrame({"Total Players": [df_Count]})
Number_Players

# Obtain number of unique items, average price, etc.

Number_Items = len(df["Item ID"].unique())

df_Price = df['Price']
Average_Price = round(df_Price.mean(), 2)

Number_Purchases = df['Purchase ID']
Count_Purchases = Number_Purchases.count()

Total_Revenue = (Count_Purchases * Average_Price)

pd.options.display.float_format = '${:,.2f}'.format
New_df = pd.DataFrame({"Number of Unique Items": [Number_Items], "Average Price": [Average_Price], 
                       "Number of Purchases": [Count_Purchases], "Total Revenue" : [Total_Revenue]})
New_df

# Percentage and Count of Male Players

# Remove duplicate from table

x = df.drop_duplicates(subset='SN', keep='first', inplace=False)

# Count Totals

Total = x["Gender"].count()
MP = x["Gender"].value_counts()['Male']
FP = x["Gender"].value_counts()['Female']
NP = Total - MP - FP

Male = (MP / Total) * 100
Female = (FP / Total) * 100
Other = (NP / Total)* 100

Gender_df = pd.DataFrame({"": ['Male', 'Female', 'Other/Non-Disclosed'],
                            "Total Count": [MP, FP, NP],
                            "Percentage of Players": [Male, Female, Other]})

# Remove Dollar sign

Gender_df["Percentage of Players"] = Gender_df["Percentage of Players"].map("{:.2f}".format)

# Display Table

Gender_df.set_index([""])

# Purchasing analysis per gender

Gender = df.groupby('Gender')
Total_Count_Gender = Gender.nunique()["SN"]

Purchase_Count = Gender["Purchase ID"].count()
Ave_Purchase_Price= Gender["Price"].mean()
Total_Purchase_Value = Gender["Price"].sum()
Ave_Purchase_Person = Total_Purchase_Value / Total_Count_Gender

Ave_Purchase_Person

# Display Data table

purchase_df = pd.DataFrame({"Purchase Count": Purchase_Count, 
                            "Average Purchase Price": Ave_Purchase_Price,
                            "Average Purchase Value": Total_Purchase_Value,
                            "Avg Purchase Total per Person": Ave_Purchase_Person})
purchase_df

# Age demographics

Age = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
Group = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

df["Age"] = pd.cut(df["Age"], Age, labels=Group)
df

Age_df = df.groupby("Age")

Total_Count_Age = Age_df["SN"].nunique()

Percentage_by_Age = (Total_Count_Age/df_Count) * 100

# Display table

Age_Demo = pd.DataFrame({"Total Count": Total_Count_Age , "Percentage of Players": Percentage_by_Age})

# Remove Index

Age_Demo.index.name = None

# Change formating

Age_Demo.style.format({"Percentage of Players":"{:,.2f}"})

# Purchasing Analysis (Age)

Total_Count_Age = Age_df.nunique()["SN"]

Age_Purchase_Age = Age_df['Purchase ID'].count()
Ave_Purchase_Age= Age_df["Price"].mean()
Total_Purchase_Age = Age_df["Price"].sum()
Ave_Purchase_Age = Total_Purchase_Age / Total_Count_Age

# Display Data table

Purchase_Age_df = pd.DataFrame({"Purchase Count": Age_Purchase_Age, 
                            "Average Purchase Price": Ave_Purchase_Age,
                            "Average Purchase Value": Total_Purchase_Age,
                            "Avg Purchase Total per Person": Ave_Purchase_Age})
Purchase_Age_df

# Top Spenders

Spenders_df = df.groupby("SN")

Spenders_Count = Spenders_df["Purchase ID"].count()
Spenders_Ave_Price = Spenders_df["Price"].mean()
Spenders_Total_Purchase = Spenders_df["Price"].sum().nlargest(5)

# Display Data table

Top_Spenders_df = pd.DataFrame({"Purchase Count": Spenders_Count, 
                               "Average Purchase Price": Spenders_Ave_Price,
                               "Total Purchase Value": Spenders_Total_Purchase})
Top_Spenders_df = Top_Spenders_df.sort_values("Total Purchase Value",ascending=False)
Top_Spenders_df.head()

# Most Popular Items

Items_df = df.groupby(["Item ID","Item Name"])

Items_Count = Items_df["Purchase ID"].count()
Items_Price = Items_df["Price"].mean()
Items_Total_Purchase = Items_df["Price"].sum()

# Display Data table

Top_Items_df = pd.DataFrame({"Purchase Count": Items_Count, 
                             "Average Purchase Price": Items_Price,
                             "Total Purchase Value": Items_Total_Purchase})
                             
# Sort descending by purchase count

Top_Items_df = Top_Items_df.sort_values("Purchase Count",ascending=False)
Top_Items_df.head()

# Most Profitable Items

Items_df = df.groupby(["Item ID","Item Name"])

Items_Count = Items_df["Purchase ID"].count()
Items_Price = Items_df["Price"].mean()
Items_Total_Purchase = Items_df["Price"].sum()

# Display Data table

Top_Items_df = pd.DataFrame({"Purchase Count": Items_Count, 
                             "Average Purchase Price": Items_Price,
                             "Total Purchase Value": Items_Total_Purchase})

# Sort descending by total purchase value

Top_Items_df = Top_Items_df.sort_values("Total Purchase Value",ascending=False)
Top_Items_df.head()
