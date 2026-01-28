def factorial(n):

    if n != 0:
        return factorial(n-1)*n
    else:
        return 1
    

if __name__ == "__main__":
    print(factorial(5))
    print(factorial(3))
    print(factorial(0))