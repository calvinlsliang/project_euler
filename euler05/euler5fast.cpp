// euler5fast.cpp
#include <iostream>
using namespace std;

bool divisible(int);

int main() {
  
  int num = 21;

  while(!divisible(num)) {
    num++;
  }

  cout << num << endl;
  return 0;
}

bool divisible(int n) {
  int k = 2;

  if (n % 11 == 0 && n % 12 == 0 && n % 13 == 0 && 
      n % 14 == 0 && n % 15 == 0 && n % 16 == 0 &&
      n % 17 == 0 && n % 18 == 0 && n % 19 == 0 &&
      n % 20 == 0) {
    return true;
  } else {
    return false;
  }
}
