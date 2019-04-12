from math import *

def prime_numbers(low, high):
    is_prime = [True]*(high+1)
    is_prime[0] = False
    is_prime[1] = False
    primes = list()
    for i in range(high):
        if is_prime[i]:
            if i > low:
                primes.append(i)
            j = 2
            while i * j < high:
                is_prime[i*j] = False
                j = j + 1
    return primes

def smallest_primitive_root(n):
    i = 2
    found = False
    spr = None
    while i < n and not found:
        powers = {pow(i, j) % n for j in range(n-1)}
        if len(powers) == n - 1:
            found = True
            spr = i
        i = i + 1
    return spr

def all_primitive_roots(n):
    spr = smallest_primitive_root(n)
    print(spr)
    exponents = filter(lambda m: gcd(m, n - 1) == 1, range(1, n))
    aprs = [int(pow(spr, s) % n) for s in exponents]
    return aprs
        
        
print(smallest_primitive_root(13))
print(all_primitive_roots(13))