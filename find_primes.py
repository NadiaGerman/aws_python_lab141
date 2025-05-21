# find_primes.py
# This script finds all prime numbers between 1 and 250 and writes them to results.txt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = [str(n) for n in range(1, 251) if is_prime(n)]

with open("results.txt", "w") as f:
    f.write("\n".join(primes))

print("Prime numbers from 1 to 250 have been written to results.txt")
