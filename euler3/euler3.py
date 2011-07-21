num = 600851475143
numf = 13195
large = 0
k=12

def isprime(n):
    i=2
    while i < n:
        if n % i == 0:
            return 0
        i+=1
    return 1

def inc(n):
    n+=1
    if isprime(n):
        return n
    return inc(n)


n=2
while num != 1:
    n = inc(n)
    while num % n == 0:
        num /= n


print n

'''
i = 2
while i < 30:
    i = inc(i)
    print i
'''
