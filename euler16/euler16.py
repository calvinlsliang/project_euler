num = 2**1000
sum = 0
while not(num/10 == 0):
    sum = sum + (num % 10)
    num /= 10

sum += num
print sum
