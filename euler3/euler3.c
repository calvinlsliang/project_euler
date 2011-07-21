// euler3.cpp
#include <stdio.h>
#include <limits.h>

long long isPrime(long long);

int main() {
 
  long long max=600851475143;
  long long factor=0;

  for (long long i = 3; i < max; i+=2) {
    if (isPrime(i)==1) {
      if (max % i == 0) {
	factor = i;
      }
    }
  }
  printf("Prime factor: %lld\n", factor);

  return 0;
}

long long isPrime(long long n) {
  for (long long i = 2; i < n; i++) {
    if (n % i == 0) {
      return 0;
    }
    
  }
  return 1;
}
