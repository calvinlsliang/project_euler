// euler20.cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main(void) {

  int sum=1;

  for (int i=1; i<=100; i++) {
    cout << sum << endl;
    sum*=i;
  }

  cout << sum << endl;
  return 0;
}
