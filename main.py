import time

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Function {func.__name__} completed in {end_time - start_time} seconds(minutes).")
    return result
def slow_function(n):
    total = 0
    for i in range(n):
        total += i
        time.sleep(0.1)
    return total

result = measure_time(slow_function, 10)