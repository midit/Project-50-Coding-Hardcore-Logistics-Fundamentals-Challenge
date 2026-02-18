import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        time.sleep(2)
        time_elapsed = time.time()-start_time
        print(f"Час виконання: {time_elapsed:.4f} сек.")
        return result
    return wrapper

@my_decorator
def test_function(a, b):
    return a+b

if __name__ == "__main__":
    test_function(4, 3)

    