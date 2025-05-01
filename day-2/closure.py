# 3. Closure
# 🔹 Là gì?
# Là hàm lồng hàm, trong đó hàm bên trong ghi nhớ biến của hàm bên ngoài dù đã kết thúc


def multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

double = multiplier(2)
print(double(5))  # 10
print(double(10))  # 20


# Ở đây double là một closure vì nó nhớ factor = 2.

# 🔹 Khi nào nên dùng?
# Khi cần ghi nhớ một tham số riêng biệt cho từng hàm

# Khi bạn muốn tạo hàm tuỳ chỉnh như nhân đôi, nhân ba, v.v.

# 🔹 Thực tế dùng closure để:
# Tạo các hàm tùy biến

# Dùng trong decorator