# n! I think

def factorial(n):
    if n==1 or n==0: return n
    if n>1: return n*factorial(n-1)

print factorial(40)/(factorial(20)*factorial(20))
