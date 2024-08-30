numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes = []
primes_ = {0}                         # множество для выборки уникальных значений                      # количество элементов списка
for i in numbers:
    k = 0                              # счетчик
    for j in range(2, i + 1):
        if i % j == 0:
            k = k + 1
            if k > 1:
                not_primes.append(i)
                break
            else:
                primes_.add(j)        # запись в множество для отсечки повторяющихся элементов
primes_.remove(0)                     # убрал 0 ( необходим был для создания множества )
primes = list(primes_)                # преобразование в список из множества
print('not_primes = ', not_primes)
print('primes = ', primes)