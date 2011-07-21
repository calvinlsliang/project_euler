// euler10.cpp
#include <iostream>
#include <iomanip>
//#include <bigint.h>
using namespace std;

bool divisible(int);
int nextPrime(int);
bool isPrime(int);

int main() {
  int prime=2;
  int twoMill=2000000;
  double sum=0;

  /*
  string tempString;
  Bigint sum("0");
  Bigint temp("0");
  */

  for (int i=2; i<2000000; i++) {
    if (isPrime(i)) {
      sum+=i;
    }
  }
  /*
  while (prime < 2000000) {
    sum+=prime;
    prime = nextPrime(prime);

    tempString=sum+prime;
    cout<<tempString<<endl;
    sum = sum+prime;
    prime = nextPrime(prime);
    */

  
  cout << setprecision(25) << sum << endl;
  return 0;
}

bool isPrime(int n) {
  int k=2;
  while (k<n) {
    if (n%k==0) {
      return false; 
    }
    k++;
  }
  return true;
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
