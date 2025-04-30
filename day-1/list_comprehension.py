#List Comprehension
squares = [x**2 for x in range(10)]
print(squares)

evens = [x for x in range(10) if x%2 == 0]
print(evens)

odd = [x for x in range(10) if x%2 == 1]
print(odd)

pairs = [(x, y) for x in [1,2,3] for y in [7,8]]
print(pairs)

words = ['hello', 'world']
upper_words = [word.upper() for word in words]
print(upper_words)

#làm phẳng
matrix = [[1,2,3], [4,5,6], [7,8,9]]
plat = [num for row in matrix for num in row]
print(plat)


# Lấy các ký tự không phải khoảng trắng
text = "Hello World"
chars = [char for char in text if char != ' ']
print(chars)

d = {'a': 1, 'b' : 2, 'c':3}
keys = [key for key in d.keys()]
print(keys)
values = [value for value in d.values()]
print(values)
