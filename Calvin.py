'''
factorial(n)
fib(n)
quicksort(arr)
mergesort(arr)
bin2dec(n)
dec2bin(n)
prime(n)
smallprime(n)
'''

def factorial(n):
    if n == 1 or n == 0: return 1
    else: return n * factorial(n-1)

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def quicksort(myList):
    if myList == []: return []       # Empty lists are sorted by definition
    pivot = myList[0]
    beforePivot = [x for x in myList[1:] if x <= pivot]
    afterPivot  = [x for x in myList[1:] if x >  pivot]
    return quicksort(beforePivot) + [pivot] + quicksort(afterPivot)

def mergesort(myList):
    if len(myList) <= 1: return myList
    middle = len(myList)/2
    left, right = [], []
#    for x in myList[:middle]: left.append(x)
#    for x in myList[middle:]: right.append(x)

    left = [x for x in myList[:middle]]
    right = [x for x in myList[middle:]]

    left = mergesort(left)
    right = mergesort(right)

    if left[len(left)-1] > right[0]: result = merge(left, right)
    else: result = append(left, right)
    return result

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    if len(left) > 0: result = append(result, left)
    else: result = append(result, right)

    return result     

def append(left, right):
    return left + right

def dec2bin(dec):
    bin = ''
    while dec != 0:
        if dec % 2 == 0: bin = '0' + bin
        else: bin = '1' + bin
        dec /= 2

    return bin

def bin2dec(bin):
    dec = 0
    p = 0
    bin = int(bin)
    while bin != 0:
        if bin % 10 == 1: dec += 2 ** p
        bin /= 10
        p += 1

    return dec

def prime(n):
    f = open('small_prime', 'r')
    a = f.read()
    a = a.split()
    for i in a:
        if str(n) == i: return True
    return False
    f.close()

def smallprime(n):
    f = open('small_prime', 'r')
    a = f.read()
    a = a.split()
    for i in a:
        if str(n) == i: return True
    return False
    f.close()
