import pandas as pd

# Create a sample dataset
data = {
    'Name': ['John', 'Emma', 'Mark', 'Emily', 'David'],
    'Age': [25, 28, 31, 24, 29],
    'City': ['New York', 'London', 'Paris', 'Sydney', 'Tokyo'],
    'Salary': [50000, 60000, 70000, 55000, 65000]
}

# Create a DataFrame from the dataset
df = pd.DataFrame(data)

# Print the DataFrame
print("Original DataFrame:")
print(df)

# Perform some operations on the DataFrame
average_age = df['Age'].mean()
max_salary = df['Salary'].max()

# Print the results
print("\nAverage Age:", average_age)
print("Maximum Salary:", max_salary)

# Filter the DataFrame based on a condition
filtered_df = df[df['Salary'] > 60000]

# Print the filtered DataFrame
print("\nFiltered DataFrame:")
print(filtered_df)
