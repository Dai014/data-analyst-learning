import csv

try:
    x = int("abc")
except ValueError as e:
    print("lỗi chuyển đổi: ", {e})


students = [
    ["name", "subject", "score"],
    ["Minh", "math", 8.5],
    ["Lan", "literature", 7.0],
    ["Nam", "physics", 9.0],
    ["Hanh", "chemistry", 6.5],
    ["Hoa", "biology", 8.0],
    ["Khanh", "history", 7.5],
    ["Tuan", "geography", 9.5],
    ["Thao", "english", 8.2],
    ["Duc", "informatics", 7.8],
    ["An", "physical education", 6.8],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)


with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"],"==>" ,row["subject"], "==>",row["score"])

try:
    with open('non_existent.csv', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File không tồn tại!")
except PermissionError:
    print("Không có quyền truy cập file!")