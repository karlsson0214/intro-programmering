# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
def is_next_prime(primes, number):
    for prime in primes:
        if number % prime == 0:
            return False
    return True

primes = [2]

for i in range(3, 10):
    if is_next_prime(primes, i):
        primes.append(i)

print(primes)
