#Task 1: Calculate Factorial Using a Function

def fact(n):
    if n<2:
        return 1
    result=1
    for i in range(2,n+1):
        result*=i
    return result

n=int(input("Enter a number: "))
factorial=fact(n)
print(f"Factorial of {n} is: {factorial}")