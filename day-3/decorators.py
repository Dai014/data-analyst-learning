def time_execution(func):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result

    return wrapper

@time_execution
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Example usage
if __name__ == "__main__":
    print(example_function(1000000))