numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = list(filter(lambda x: all(x % i != 0 for i in range(2, x)), numbers))
print("Prime numbers in the list:", primes)