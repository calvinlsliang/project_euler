// euler13.cpp
#include <iostream>
#include <fstream>
#include <cstdlib>
#include "bigint.h"
using namespace std;

int main() {
  Bigint sum(0);
  Bigint x(0);
  ifstream file;

  file.open("test.txt");
  if (!file) {
    cout << "Unable to open file test.txt";
    exit(1);
  }
  
  while (file >> x) {
    sum = sum + x;
  }

  file.close();

  cout << sum << endl;

  return 0;
}
