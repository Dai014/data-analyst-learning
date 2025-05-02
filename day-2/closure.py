# Closure (đóng gói) là một hàm bên trong (inner function) có khả năng "nhớ" 
# các biến từ phạm vi bao quanh (enclosing scope) của nó, 
# ngay cả khi hàm bên ngoài đã kết thúc thực thi.
# Nói đơn giản, Closure là một hàm giữ được trạng thái của các biến mà nó 
# tham chiếu từ môi trường xung quanh.

# Closure thường được dùng để:
# Lưu trữ trạng thái mà không cần biến toàn cục.
# Tạo các hàm với hành vi tùy chỉnh.
# Ẩn dữ liệu (data hiding) để bảo vệ trạng thái.

# Hãy nghĩ Closure như một chiếc "ba lô" mà hàm bên trong mang theo, chứa các biến từ hàm
# bên ngoài để sử dụng sau này.

def outer_function():
    variable = 5
    def inner_function():
        # Sử dụng variable từ outer_function
        return variable
    return inner_function

def make_multiplier(n):
    def multiplier(x):
        return x * n # multiplier "nhớ" n
    return multiplier

times_two = make_multiplier(2) # times_two là một hàm closure
times_three = make_multiplier(3)

print(times_two(5))  # Kết quả: 10, vì 5 * 2 = 10, 2 được nhớ trong closure
print(times_three(5))  # Kết quả: 15, vì 5 * 3 = 15, 3 được nhớ trong closure


def make_counter():
    count = 0
    def counter():
        nonlocal count  # Cho phép sửa biến từ phạm vi ngoài
        count += 1
        return count
    return counter

counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 (counter2 có trạng thái riêng)

# counter là Closure, nhớ giá trị count từ make_counter.
# nonlocal cho phép counter sửa đổi count.
# Mỗi Closure (counter1, counter2) có bản sao riêng của count, nên chúng hoạt động độc lập.


# 6. Khi nào nên dùng Closure?
# Lưu trạng thái mà không dùng biến toàn cục: Ví dụ, đếm số lần gọi, lưu cấu hình.
# Tạo hàm tùy chỉnh: Ví dụ, tạo các hàm với hành vi khác nhau dựa trên tham số.
# Ẩn dữ liệu (data hiding): Biến trong Closure không thể truy cập từ bên ngoài.
# Viết Decorator: Closure là nền tảng của Decorator trong Python.

def make_logger(level):
    def log(message):
        return f"[{level}] {message}"
    return log

debug = make_logger("DEBUG")
error = make_logger("ERROR")

print(debug("This is a debug message"))  # [DEBUG] This is a debug message
print(error("This is an error message"))  # [ERROR] This is an error message


# 7. Closure trong Decorator

def check_positive(func):
    def wrapper(*args):
        if all(arg > 0 for arg in args):
            return func(*args)
        return "Tất cả tham số phải dương!"
    return wrapper

@check_positive
def add(a, b):
    return a + b

print(add(2, 3))  # 5
print(add(-1, 3)) # Tất cả tham số phải dương!
# wrapper là Closure, nhớ hàm func từ check_positive.
# wrapper thêm logic kiểm tra trước khi gọi func.

# Closure khác hàm thông thường như thế nào?
# Hàm thông thường không "nhớ" trạng thái từ phạm vi ngoài sau khi hàm cha kết thúc. Closure lưu trữ trạng thái thông qua cell object.
# Closure có phải là Decorator?
# Không, nhưng Closure là nền tảng của Decorator. Decorator sử dụng Closure để lưu hàm gốc và thêm hành vi.
# Làm sao để kiểm tra Closure?
# Dùng func.__closure__ để xem các biến được lưu trữ, hoặc func.__code__.co_freevars để xem tên các biến tự do.