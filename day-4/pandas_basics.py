import pandas as pd



# df = pd.read_csv("students.csv")

# print(df[df["score"] > 8.0]["name"])

# # Hiển thị 5 dòng đầu
# print(df.head())


# # Thống kê cơ bản
# print(df.describe())

# print(df["score"].mean()) # Tính điểm trung bình

# df[df["score"] > 7].to_csv("students_pass.csv", index=False) 

# df[df["score"] > 7].to_json("students_pass.json", orient="records", lines=True)




# tạo dataframe Từ dict
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'London', 'Paris']
}

# df = pd.DataFrame(data)
# print(df.head())

dataFrame = pd.read_csv("data.csv")


print(dataFrame.dtypes) # Kiểm tra kiểu dữ liệu của các cột

dataFrame["age"] = dataFrame["age"].astype(float) # Chuyển đổi kiểu dữ liệu của cột age thành float
print(dataFrame.dtypes) # Kiểm tra kiểu dữ liệu của các cột sau khi chuyển đổi
dataFrame['age'] = dataFrame["age"].astype("category") 
print(dataFrame.dtypes)# Chuyển đổi kiểu dữ liệu của cột age thành category
dataFrame = dataFrame.astype({'age':'float', 'city':'category'}) # Chuyển đổi nhiều cột cùng lúc)
print(dataFrame.dtypes) # Kiểm tra kiểu dữ liệu của các cột sau khi chuyển đổi
print(dataFrame.index)
dataFrame.set_index("name", inplace=True) # Đặt cột name làm chỉ mục
print(dataFrame.index)
dataFrame = dataFrame.reset_index()
print(dataFrame.index)
print(dataFrame.columns)
dataFrame.columns = ['full_name', 'years', 'location', 'income']
print(dataFrame)
dataFrame.rename(columns={'income': 'wage'}, inplace=True) # Đổi tên cột years thành age
print(dataFrame)


dataFrame.columns = pd.read_csv("data.csv").columns # Đổi tên cột bằng cách đọc từ file csv khác
print(dataFrame.columns)

dataFrame = dataFrame.set_index("name") # Đặt cột name làm chỉ mục

print(dataFrame.at["Bob", "salary"])
dataFrame.at["Bob", "salary"] = 8888888
print(dataFrame.at["Bob", "salary"])
print(dataFrame) # Truy cập giá trị tại hàng thứ 1 và cột thứ 2

print(dataFrame.loc['Bob'])
print(dataFrame.loc['Bob', 'salary'])
print(dataFrame.loc[['Bob', 'Alice']]) # Truy cập nhiều hàng và cột

print(dataFrame.loc[['Bob','David'], ['city']]) # Truy cập nhiều hàng và cột

# print(dataFrame.iloc[0]) # Truy cập hàng đầu tiên
print(dataFrame.iloc[0:2]) # Truy cập hàng từ 0 đến 2 (không bao gồm 2)
print(dataFrame.iloc[0, 0:2]) # Truy cập hàng từ 0 đến 2 (không bao gồm 2) và cột từ 0 đến 2 (không bao gồm 2)
print(dataFrame.iloc[0, [0, 2]]) # Truy cập hàng đầu tiên và cột 0 và 2

print("bat dau lai tu day");



# print(dataFrame.iloc[0:2, 1]) 
dataFrame.iloc[2,0]= 36 # Truy cập hàng thứ 2 và cột thứ 1
print(dataFrame.iloc[2,0]) # Truy cập hàng từ 0 đến 2 (không bao gồm 2) và cột thứ 1