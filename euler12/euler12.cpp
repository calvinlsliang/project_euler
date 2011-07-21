// euler12.cpp
#include <iostream>
#include <math.h>
using namespace std;

int factors(int n)
{
  int counter = 0;
  for (int i = 1; i < (sqrt(n)+1); i++) {
    if (n % i == 0) {
      counter+=2;
    }
  }
  return counter;
}


int main() {
  
  int n = 2;
  int tri = 1;
  
  while (factors(tri) < 500) {
    tri+= n;
    n++;
  }

  cout << tri << endl;

  return 0;
}
