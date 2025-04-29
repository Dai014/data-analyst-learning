from time import time
from functools import wraps

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

@log_execution_time
def example_api_function(data):
    # Simulate processing time
    total = sum(data)
    return total

if __name__ == "__main__":
    # Example usage
    data = range(1000000)
    result = example_api_function(data)
    print(f"Result: {result}")