// euler6.cpp
#include <iostream>
using namespace std;

int square(int);

int main() {

  int sum = 0, sum1 = 0, tempSum = 0, sum2 = 0;
  
  // Sum of the square
  for (int i = 1; i < 101; i++) {
    sum1 += square(i);
  }

  // Square of the sum
  for (int i = 1; i < 101; i++) {
    tempSum += i;
  }

  sum2 = square(tempSum);

  sum = sum2 - sum1;

  cout << sum << endl;
  return 0;
}

int square(int n) {
  return n*n;
}
