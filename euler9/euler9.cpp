// euler9.cpp
#include <iostream>
using namespace std;

int square(int);
bool pythag(int, int, int);

int main() {
 
  const int SUM = 1000;
  int a = 0, b = 0, c = 0;
  int product;

  for (int x = 1; x < SUM; x++) {
    for (int y = 1; y < SUM; y++) {
      for (int z = 1; z < SUM; z++) {
	if (x + y + z == SUM) {
	  if (pythag(x, y, z)) {
	    a = x;
	    b = y;
	    c = z;
	  }
	}
      }
    }
  }

  product = a * b * c;
  cout << a << " " << b << " " << c << endl;
  cout << product << endl;
  return 0;
}

int square(int x) {
  return x * x;
}

bool pythag(int x, int y, int z) {
  return ((square(x) + square(y)) == square(z));
}
