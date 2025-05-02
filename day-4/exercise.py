import pandas as pd

# Tạo DataFrame mới từ danh sách
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df2 = pd.DataFrame(data)


try: 
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    exit()


# Đặt index tùy chỉnh
df.set_index('name', inplace=True)

# Dùng loc để truy cập hàng có index là 'Bob'
print(df.loc['Bob'])

df = pd.read_csv("data.csv")
df.set_index("name", inplace=True) # Đặt cột name làm chỉ mục
print(df.dtypes)
df['salary'] = df['salary'].astype(float)
print(df.dtypes)
df = df.rename(columns={'city': 'location'})
print(df)

print("bai 2")
print(df.at["Charlie", "salary"]) # Truy cập giá trị tại hàng thứ 1 và cột thứ 2

# Lấy các hàng có age >= 30
print(df.loc[df['age'] >= 30])

# Dùng iloc để lấy 2 hàng đầu, 2 cột cuối.
print(df.iloc[0:2, -2:])

df.loc[df['salary'] > 55000].to_csv("high_salary.csv") # Truy cập nhiều hàng và cột

print("bat dau lai tu day")

print("==========================")



# Cách 1: df['name']
result1 = df[df['age'] >= 30]['name']
print(result1)  # Series
print(type(result1))  # <class 'pandas.core.series.Series'>

# Cách 2: df.loc
result2 = df.loc[df['age'] >= 30, 'name']
print(result2)  # Series
print(type(result2))  # <class 'pandas.core.series.Series'>

# Cách 3: df[['name']]
result3 = df[df['age'] >= 30][['name']]
print(result3)  # DataFrame
print(type(result3))  # <class 'pandas.core.frame.DataFrame'>