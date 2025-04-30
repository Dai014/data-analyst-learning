# Decorator là một công cụ trong Python cho phép bạn mở rộng hoặc thay đổi hành vi của một hàm (hoặc phương thức) 
# mà không cần sửa đổi trực tiếp mã nguồn của hàm đó. Nó giống như một "vỏ bọc" (wrapper) bọc quanh hàm để thêm chức năng bổ sung, chẳng hạn như đo thời gian chạy, kiểm tra quyền, ghi log, hoặc xử lý lỗi.
# Decorator sử dụng Closure (hàm bên trong nhớ trạng thái từ hàm bên ngoài) để hoạt động.
# Trong Python, Decorator thường được áp dụng bằng cú pháp @decorator_name đặt phía trên định nghĩa hàm.
# Hãy nghĩ Decorator như một món quà: Hàm gốc là món quà, còn Decorator là giấy gói thêm vào để làm món quà đẹp hơn hoặc thêm tính năng mới.


# 2. Tại sao cần Decorator?
# Decorator giúp mã:

# Tái sử dụng: Áp dụng cùng một logic bổ sung (như logging, kiểm tra) cho nhiều hàm.
# Sạch sẽ: Không cần sửa đổi mã hàm gốc, giữ mã dễ bảo trì.
# Tách biệt trách nhiệm: Tách logic chính của hàm và logic bổ sung (như kiểm tra đầu vào, đo thời gian).
# Ví dụ, thay vì thêm mã đo thời gian vào từng hàm, bạn có thể viết một Decorator và áp dụng nó cho bất kỳ hàm nào cần.

# 3. Cách hoạt động của Decorator
# Decorator là một hàm nhận một hàm khác làm đầu vào, bọc nó bằng một hàm mới (wrapper), và trả về hàm wrapper đó. Hàm wrapper có thể thêm logic trước, sau, hoặc thay đổi kết quả của hàm gốc.

# Định nghĩa một decorator
def my_decorator(func):
    def wrapper():
        print("Trước khi gọi hàm")
        func()
        print("Sau khi gọi hàm")
    return wrapper


# Sử dụng decorator
@my_decorator
def say_hello():
    print("Xin chào!")

# Gọi hàm
say_hello()

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} chạy mất {end - start:.2f} giây")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Xong"

print(slow_function())
# Output:
# slow_function chạy mất 1.00 giây
# Xong

# 5. Decorator với tham số
# Đôi khi bạn muốn Decorator nhận tham số để tùy chỉnh hành vi. Để làm điều này, cần thêm một lớp hàm nữa (decorator factory).

def decorator_with_args(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Sử dụng arg và gọi func
            return func(*args, **kwargs)
        return wrapper
    return decorator

def limit_calls(max_calls):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            if count < max_calls:
                count += 1
                return func(*args, **kwargs)
            return "Đã vượt quá số lần gọi!"
        return wrapper
    return decorator

@limit_calls(2)
def say_hello():
    return "Hello!"

print(say_hello())  # Hello!
print(say_hello())  # Hello!
print(say_hello())  # Đã vượt quá số lần gọi!

# 9. Khi nào nên dùng Decorator?
# Thêm chức năng chung: Đo thời gian, ghi log, kiểm tra quyền, xử lý lỗi.
# Kiểm tra đầu vào: Đảm bảo tham số hợp lệ trước khi gọi hàm.
# Tái sử dụng mã: Áp dụng cùng logic cho nhiều hàm.
# Tăng tính mô-đun: Tách biệt logic chính và logic bổ sung.