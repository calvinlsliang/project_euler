// euler7.cpp
#include <iostream>
using namespace std;

bool divisible(int);
bool isPrime(int);
int nextPrime(int);

int main() {
  int range = 1, prime = 2;

  while (range < 10001) {
    prime = nextPrime(prime);
    range++;
  }  
 
  cout << prime << endl;
  return 0;
}

bool divisible(int n) {
  int k = 2;
  while(k < n) {
    if (n % k == 0) {
      return true;
    }
    k++;
  }
  return false;
}

int nextPrime(int n) {
  int k = n + 1;

  while(divisible(k)) {
    k++;
  }
  return k;
}
