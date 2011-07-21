// euler5.cpp
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
  int k = 1;
  while(k < 21) {
    if (!(n % k == 0)) {
      return false;
    }
    k++;
  }
  return true;
}
