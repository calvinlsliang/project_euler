// euler.cpp
#include <iostream>
using namespace std;

int fib(int);

int main() {

  int total = 2;
  int x = 5;

  while (fib(x) < 4000000) {

    int y = fib(x);
    if (y % 2 == 0) {
      total += y;
    }

    x++;

  }

  cout << total << endl;

  return 0;

}

int fib(int n) {
  int f[n+1];
  f[1] = f[2] = 1;
  for (int i = 3; i <= n; i++) {
    f[i] = f[i-1] + f[i-2];
  }
  return f[n];
}
