import time
def decorator(func):
    def wrapper(*args, **kwargs):
        start_time=time.perf_counter()
        result=func(*args, **kwargs)
        end_time=time.perf_counter()
        duration = end_time-start_time
        print(f"Name: {func.__name__} , Duration: {duration: .6f} seconds ")
        return result
    return wrapper
        

@decorator
def factorial(n):
    # 1. Base Case: Stop the recursion
    if n == 1:
        return 1
    
    # 2. Recursive Step: Call the function with n-1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))