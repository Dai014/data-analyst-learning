import pandas as pd

def increaseSalary(salary):
    return salary * 1.1

df = pd.read_csv("employees.csv")

def increase_salary(salary):
    return salary * 1.1

df['new_salary'] = df['salary'].apply(increase_salary)

# print(df[['name', 'salary', 'new_salary']])

# Tính lương trung bình sau khi tăng 10% theo department:
groupedDepartment = df.groupby('department')
print(df.groupby('department')['salary'].apply(lambda x: (x * 1.1).mean()))

print(groupedDepartment['new_salary'].mean()) # Tính lương trung bình theo phòng ban
print(groupedDepartment['salary'].apply(lambda x: (x*1.1).mean())) # Tính lương trung bình theo phòng ban

# Bài tập
# Dùng apply để tạo cột age_group (Young nếu age < 30, Senior nếu age >= 30).
# Dùng apply để chuẩn hóa tên (viết hoa chữ cái đầu).
# Dùng apply trên nhóm để tính độ lệch chuẩn của salary theo department.

df['age_group'] = df['age'].apply(lambda x: 'Young' if x <30 else 'Senior')

print(df[['name', 'age', 'age_group']])

print(df['name'].apply(lambda x: x.title())) # Viết hoa chữ cái đầu