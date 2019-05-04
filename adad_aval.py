import math
import random


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_2(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True

lst=[random.randint(2,10000) for i in range(10000)]

prime_list=[i for i in lst if is_prime(i)]
print(prime_list)


prime_list=[i for i in lst if is_prime_2(i)]
print(prime_list)

