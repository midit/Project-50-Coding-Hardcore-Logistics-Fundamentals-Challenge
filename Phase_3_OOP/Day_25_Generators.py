def fibonacci_generator(n):
    a, b = 0,1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == "__main__":
    for num in fibonacci_generator(10):
        print(num, end=", ")
    print("\n")
    for num in fibonacci_generator(22):
        print(num, end=", ")
    print("\n")
    for num in fibonacci_generator(8):
        print(num, end=", ")
    
    