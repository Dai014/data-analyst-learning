import pandas as pd

# employees = pd.DataFrame({
#     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'age': [25, 30, 35, 28, 40],
#     'city': ['New York', 'London', 'Paris', 'Tokyo', 'London'],
#     'salary': [50000, 60000, 75000, 55000, 80000],
#     'department': ['HR', 'IT', 'IT', 'HR', 'IT']
# })                                                          
# employees.to_csv("employees.csv", index=False)


# departments = pd.DataFrame({
#    'department': ['HR', 'IT'],
#     'manager': ['John', 'Mary']
# })
# departments.to_csv("departments.csv", index=False)

df = pd.read_csv("employees.csv")

groupedDepartment = df.groupby('department')
# print(groupedDepartment['salary'].mean()) # Tính lương trung bình theo phòng ban
# print(groupedDepartment['salary'].sum()) # Tính tổng lương theo phòng ban
# print(groupedDepartment['salary'].max()) # Tính lương cao nhất theo phòng ban
# print(groupedDepartment['salary'].min()) # Tính lương thấp nhất theo phòng ban

print(df.groupby(['city', 'department'])['salary'].mean()) # Tính lương trung bình theo thành phố và phòng ban

# Tính tuổi trung bình theo department.
# Tính tổng salary theo city.
# Nhóm theo department và đếm số nhân viên trong mỗi nhóm:

print(groupedDepartment['age'].mean()) # tinh tuoi trung binh theo department

groupedCity = df.groupby('city')
print(groupedCity['salary'].sum()) # Tinh tong salary theo city
print(groupedDepartment['name'].count()) # Dem so nhan vien theo department