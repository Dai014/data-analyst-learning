import pandas as pd

df1 = pd.read_csv('employees.csv')
df2 = pd.read_csv('departments.csv')
df3 = pd.read_csv('bonuses.csv')

employees_departments = pd.merge(df1, df2, on='department', how='inner')
print(employees_departments)

# employees_bonuses = pd.merge(df1, df3, on='name', how='inner')
# print(employees_bonuses)

df2 = df2.set_index('department')
df1 = pd.read_csv('employees.csv').set_index('department')

joined_df12 = df1.join(df2, on='department', how='left')
print(joined_df12)

joined_df12_ = df1.join(df2, on='department', how='inner')
print(joined_df12_)