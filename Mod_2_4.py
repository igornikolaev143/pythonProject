numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
k = 0
for i in range(2, k // 2+1):
    if (k % i == 0):
        k = k+1
if (k <= 0):
    print('primes: = []')
else:
    #print('not_primes: = []')
