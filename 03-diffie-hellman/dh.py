from math import *
from random import *

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
    i = 1
    found = False
    spr = None
    while i < n and not found:
        powers = {i**j % n for j in range(n-1)}
        if len(powers) == (n - 1):
            found = True
            spr = i
        i = i + 1
    return spr

def all_primitive_roots(n):
    spr = smallest_primitive_root(n)
    exponents = filter(lambda m: gcd(m, n - 1) == 1, range(1, n))
    aprs = [int(pow(spr, s) % n) for s in exponents]
    return aprs
        
p = sample(prime_numbers(10, 100), 1)[0]
g = sample(all_primitive_roots(p),1)[0]

print("- Shared: ")
print("p:\t",p)
print("g:\t",g)

print("- A: (send)")
s = randint(1, p - 2)
S = g ** s % p
print("secret:\t", s)
print("send:\t", S)

print("- B: (send)")
h = randint(1, p - 2)
H = g ** h % p
print("secret:\t", h)
print("send:\t", H)

print("- A: (receive)")
k_a = H**s % p
print("key:\t", k_a)

print("- B: (receive)")
k_b = S**h % p
print("key:\t", k_b)

if k_a != k_b:
    print("Err. Something wrong?!")