import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


'''-------------------------------------------------------'''
"1.1 Load the CSV file"
df = pd.read_csv("supermarket_sales_case_study.csv")

"1.2 Check number of rows and columns"
# print("Total Rows & Column's",df.shape)

"First few row"
# print("First Few Rows",df.head(5))

"1.3 Each column's data types"
# print("Data Type Each Column's",df.dtypes)
'''--------------------------------------------------------'''







'''--------------------------------------------------------'''
"2.1 Missing values in each column" 
# print("Missing Value Each Column's",df.isna().sum())

"2.2 Exact duplicate rows"
# print("Exact Duplicated Roes",df.duplicated().sum())

"2.3"
'''---------------------------------------------------------'''








'''-----------------------------------------------------------'''
"3.1 Drop exact duplicates"
# print("Before Drop Duplicated",df.duplicated().sum())
# df = df.drop_duplicates()
# print("After Drop Duplicated",df.duplicated().sum())

'''-----------------------------------------------------------'''








'''------------------------------------------------------------'''
"4.1 Resolve conflicting Invoice IDs"

'''----------Rule: If an Invoice ID appears more than once,
keep the last row because it contains the latest correction.---------'''

# print("before_rows",len(df))
# df = df.drop_duplicates(subset="Invoice ID", keep="last")
# print("after_rows",len(df))
'''-----------------------------------------------------------'''








'''-----------------------------------------------------------'''
"5.1 Standardise text columns"
# df['Gender'] = df['Gender'].str.strip().str.lower() 
# print(df['Gender'])

# df['Gender'] = df['Gender'].replace({
#     'male' : 'Male',
#     'female' : 'Female'
# })

# print(df["Gender"])


# df['Payment'] = df['Payment'].str.strip().str.lower()
# print(df['Payment'])

# df['Payment'] = df["Payment"].replace({
#     'cash' : 'Cash',
#     'credit card' : 'Credit card',
#     'ewallet' : 'Ewallet'
# })
# print(df["Payment"])
'''-----------------------------------------------------------'''









'''-----------------------------------------------------------'''
# "6.1 Fix negative quantities"
# df['Quantity'] = df['Quantity'].abs() 
# print(df['Quantity'])
'''-----------------------------------------------------------'''








'''-----------------------------------------------------------'''
"7. Parse mixed dates"
# dates = df['Date'].copy()

# df['Date'] = pd.to_datetime(
#     dates, format='%m/%d/%Y', errors='coerce'
# )

# df['Date'] = df['Date'].fillna(
#     pd.to_datetime(dates, format='%d-%m-%Y', errors='coerce')
# )

# print(df['Date'])

'''-----------------------------------------------------------'''







'''------------------------------------------------------------'''
"8.1 Check Total"
# print(df['Total'])
# print(df['Quantity'] * df['Unit price'] * 1.05)
'''------------------------------------------------------------'''








'''-------------------------------------------------------------'''
"9.1 Handle what is still missing"
# df['Customer type'] = df["Customer type"].fillna('Unkown')
# print(df["Customer type"])

# df['Rating'] = df['Rating'].fillna(df['Rating'].median())
# print(df['Rating'])

# df = df.dropna(subset=['Date'])
# print(df.isnull().sum())
'''-------------------------------------------------------------'''








'''--------------------------------------------------------------'''
"10. Keep an audit trail"
# print("Before Rows",len(df))
# before = len(df)

# df = df.drop_duplicates()

# print("After Rows",len(df))
# after = len(df)

# print("Removed Rows",before - after)
'''----------------------------------------------------------------'''
#                     "Cleaning Completed"                           #
'''-----------------------------------------------------------------'''









"----------------------'''Answering the brief'''--------------------"
"1.1 Add time columns."
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# df['Time'] = pd.to_datetime(
#     df['Time'], format='%H:%M:%S', errors='coerce'
# )

# df['Year'] = df['Date'].dt.year

# df['Quarter'] = (
#     df['Date'].dt.year.astype('Int64').astype(str)
#     + 'Q'
#     + df['Date'].dt.quarter.astype('Int64').astype(str)
# )

# df['Day of week'] = df['Date'].dt.day_name()

# df['Hour'] = df['Time'].dt.hour

# print(df[['Date', 'Time', 'Year', 'Quarter',
#           'Day of week', 'Hour']].head())

'''-----------------------------------------------------------------'''








'''-----------------------------------------------------------------'''
"2.1 Bucket the trading day"
# df['Trading Day'] = np.select(
#     [
#         df['Hour'].between(10, 12),
#         df['Hour'].between(13, 16),
#         df['Hour'].between(17, 20)
#     ],
#     [
#         'Morning',
#         'Afternoon',
#         'Evening'
#     ],
#     default='Outside Hours'
# )

# transactions = df['Trading Day'].value_counts()

# hours = {
#     'Morning': 3,
#     'Afternoon': 4,
#     'Evening': 4
# }

# for bucket, duration in hours.items():
#     count = transactions.get(bucket, 0)
#     print(bucket, "Transactions:", count)
#     print(bucket, "Transactions per hour:", count / duration)
'''------------------------------------------------------------------'''








'''------------------------------------------------------------------'''
# "3.1  Compare against target"
# revenue = (
#     df.groupby(['Branch', 'Quarter'], as_index=False)['Total']
#       .sum()
#       .rename(columns={'Total': 'Revenue'})
# )

# branches = df['Branch'].dropna().unique()

# targets = pd.DataFrame({
#     'Branch': branches,
#     'Target': 100000
# })

# result = revenue.merge(targets, on='Branch', how='left')

# result['Variance'] = result['Revenue'] - result['Target']

# result['% of target'] = (
#     result['Revenue'] / result['Target'] * 100
# )

# result['Hit'] = result['Revenue'] >= result['Target']

# print(result)

'''-------------------------------------------------------------------'''








'''-------------------------------------------------------------------'''
# "4.1 Summarise each branch"
# quarterly = df.groupby(['Branch', 'Year', 'Quarter'])['Total'].sum().reset_index()

# for branch in df['Branch'].unique():

#     data = quarterly[quarterly['Branch'] == branch]

#     average = data['Total'].mean()

#     quarters = (data['Total'] > 0).sum()

#     best = data.loc[data['Total'].idxmax(), 'Quarter']
#     worst = data.loc[data['Total'].idxmin(), 'Quarter']

#     rev_2023 = data[data['Year'] == 2023]['Total'].sum()
#     rev_2024 = data[data['Year'] == 2024]['Total'].sum()

#     if rev_2023 != 0:
#         growth = (rev_2024 / rev_2023 - 1) * 100
#     else:
#         growth = 0

#     print("Branch:", branch)
#     print("Average Revenue:", average)
#     print("Quarters hit out of 8:", quarters)
#     print("Best Quarter:", best)
#     print("Worst Quarter:", worst)
#     print("YoY Growth:", round(growth, 2), "%")
#     print("--------------------")

'''--------------------------------------------------------------------'''










'''--------------------------------------------------------------------'''
"5.1 Find the busy times"

# quarterly = df.groupby(['Branch', 'Year', 'Quarter'])['Total'].sum().reset_index()

# for branch in df['Branch'].unique():

#     data = quarterly[quarterly['Branch'] == branch]

#     print("Branch:", branch)
#     print("Average Revenue:", data['Total'].mean())

#     print("Quarters hit:", (data['Total'] > 0).sum())

#     print("Best Quarter:", data.loc[data['Total'].idxmax(), 'Quarter'])
#     print("Worst Quarter:", data.loc[data['Total'].idxmin(), 'Quarter'])

#     rev_2023 = data[data['Year'] == 2023]['Total'].sum()
#     rev_2024 = data[data['Year'] == 2024]['Total'].sum()

#     if rev_2023 > 0:
#         growth = (rev_2024 / rev_2023 - 1) * 100
#         print("YoY Growth:", round(growth, 2), "%")
#     else:
#         print("YoY Growth: N/A")

#     print("--------------------")

'''-------------------------------------------------------------------'''









'''--------------------------------------------------------------------'''
"6.1 Chart, export, summarise"

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Year'] = df['Date'].dt.year
df['Quarter'] = (
    df['Year'].astype('Int64').astype(str)
    + 'Q'
    + df['Date'].dt.quarter.astype('Int64').astype(str)
)

quarterly = df.groupby(
    ['Branch', 'Year', 'Quarter']
)['Total'].sum().reset_index()

for branch in quarterly['Branch'].unique():

    data = quarterly[quarterly['Branch'] == branch]

    plt.plot(data['Quarter'], data['Total'], marker='o')
    plt.axhline(y=100000, color='red')
    plt.title(branch)
    plt.xlabel('Quarter')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

df.to_csv('clean_data.csv', index=False)

print("1. Total branches:", df['Branch'].nunique())
print("2. Total revenue:", df['Total'].sum())
print("3. Average revenue:", df['Total'].mean())
print("4. Best branch:", df.groupby('Branch')['Total'].sum().idxmax())
print("5. Lowest revenue branch:", df.groupby('Branch')['Total'].sum().idxmin())
'''-------------------------------------------------------------------'''
#                        Assignment Completed                           #
'''-------------------------------------------------------------------'''



