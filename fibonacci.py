def sequence(n):

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return sequence(n-1) + sequence(n-2)
        
def factorial(n):
    for i in range(1, n+1):
        fact = fact * i

    return fact