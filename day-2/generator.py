from itertools import islice

def count_up_to(n):
    for i in range(n):
        yield i
gen = count_up_to(5)
print(next(gen))

def fibonacci(n):
    a, b = 0, 1
    while True: 
        yield a
        a, b = b, a + b

fib = fibonacci(10)

gen2 = (x**2 for x in range(4))  #generator expression
print(list(gen2))

evens = (x for x in range(10) if x %2 == 0)
print(list(evens))

def counter():
    count = 0
    while count < 20:
        received = yield count
        if received is not None:
            count = received
        else:
            count += 1

c = counter()
print(list(c))
print(next(c))
c.close()


def infinite_primes():
    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Lấy 5 số nguyên tố đầu tiên
primes = list(islice(infinite_primes(), 5))
print(primes)  
