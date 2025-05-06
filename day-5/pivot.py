import pandas as pd

df = pd.read_csv("employees.csv")
# print(df)

pivot_table = df.pivot(index='name', columns='department', values='salary')
# print(pivot_table)

pivot_table2 = df.pivot_table(index='department', columns='city', values='salary', aggfunc='mean')
# print(pivot_table2)

# Gộp dữ liệu
grouped = df.groupby(['department', 'city'])['salary'].mean().reset_index()
print(grouped)

pivot_table3 = grouped.pivot(index='department', columns='city', values='salary')
print(pivot_table3)