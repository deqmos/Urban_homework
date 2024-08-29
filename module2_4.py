def prime(n):
    return n > 1 and all(n % j != 0 for j in range(2, int(n ** 0.5) + 1))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if prime(numbers[i]):
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print(f"Primes {primes}")
print(f"Not Primes {not_primes}")
