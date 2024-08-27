numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
not_primes = {0}
primes = {0}
is_prime = True
for i in range(1, 16):
    if i == 1:
        continue
    for j in range(1, 16):
        if j == 1:
            continue
        is_prime = (j % i == 0 and j != i)
        if not is_prime:
            continue
        else:
            not_primes.add(j)
not_primes.discard(0)
primes = numbers - not_primes
primes.discard(1)
print('Primes : ', primes)
print('Not Primes : ', not_primes)
