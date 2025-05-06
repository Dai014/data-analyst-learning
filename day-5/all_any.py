import pandas as pd

df = pd.read_csv("employees.csv")
print(df['salary'] > 60000)
print((df["salary"] >= 60000).all()) # Kiểm tra xem tất cả các giá trị trong cột salary đều khác 0 hay không
print((df["salary"] >= 60000).any()) # Kiểm tra xem tất cả các giá trị trong cột salary đều khác 0 hay không

print((df.groupby("department")["age"].apply(lambda x: (x>30).all()))) # Kiểm tra xem tất cả các giá trị trong cột age đều lớn hơn 30 hay không theo từng department

# Kiểm tra xem có bất kỳ nhân viên nào ở London có salary > 70000 không.
# Kiểm tra xem tất cả nhân viên trong HR có age < 40 không.
# Dùng any để kiểm tra nếu có city nào xuất hiện nhiều hơn một lần.

# Kiểm tra xem có bất kỳ nhân viên nào ở London có salary > 70000 không
print(((df["city"] == "London") & (df["salary"] > 70000)).any()) # Kiểm tra xem có bất kỳ nhân viên nào ở London có salary > 70000 không

# Kiểm tra xem tất cả nhân viên trong HR có age > 40 không.

print(df.loc[(df["department"] == "HR") & (df["age"] < 40), ["name", "age"]])

# Kiểm tra xem tất cả nhân viên trong HR có age < 40 không
print((df.loc[df["department"] == "HR", "age"] < 40).all())
print(df[[]]) # Kiểm tra xem tất cả nhân viên trong HR có age < 40 không

result = (df.query("department == 'HR'")["age"] > 40).all()
print(result)

result2 = df.groupby("department")["age"].apply(lambda x: (x < 40).all())["HR"]
print(result2)

# Dùng any để kiểm tra nếu có city nào xuất hiện nhiều hơn một lần.


groupedCity = df.groupby("city")
print((groupedCity["city"].count() > 1).any() ) 

print(groupedCity["city"].apply(lambda x: x.count() > 1).any()) # Kiểm tra xem có city nào xuất hiện nhiều hơn một lần không