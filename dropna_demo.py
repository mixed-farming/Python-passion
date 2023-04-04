import pandas as pd

'''
is a function that is used to remove missing or null values from a DataFrame or Series.
This function can be useful when dealing with datasets that contain missing or incomplete data, as it allows you to clean and prepare the data for analysis.
'''

# create a DataFrame with missing values
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 28, 32, None, 24],
        'Country': ['USA', None, 'UK', 'Canada', 'USA']}
df = pd.DataFrame(data)

# display the original DataFrame
print(df)

# drop rows with missing values
df = df.dropna()

# display the cleaned DataFrame
print(df)
