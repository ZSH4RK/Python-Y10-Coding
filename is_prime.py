import math
def is_prime(num):
    maximum = math.ceil(math.sqrt(num))

    for i in range(2, maximum+1):
        if num % i = 0:

            return "not prime"

    print("it is prime")

num = int(input())
print(is_prime(num))
