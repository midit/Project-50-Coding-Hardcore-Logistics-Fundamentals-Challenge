"""
DAY 01: FizzBuzz
Task: Print numbers 1 to n. 
- For multiples of 3, print "Fizz". 
- For multiples of 5, print "Buzz". 
- For multiples of both, print "FizzBuzz".
Constraint: Manual implementation without AI.
"""

def fizz_buzz(n):
    for i in range(1, n + 1):
        result = ""
        if i % 3 == 0: result += "Fizz"
        if i % 5 == 0: result += "Buzz"
        print(result or i)

if __name__ == "__main__":
    fizz_buzz(15)