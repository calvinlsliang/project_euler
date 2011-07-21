// euler21.cpp
#include <iostream>
using namespace std;

int divisors(int n) {
  int sum=0;
  for (int i=1; i<(n/2)+1; i++) {
    if (n%i==0) {
      sum+=i;
    }
  }
  return sum;
}

int main(void) {
  int sum=0, pair;

  for (int i=1; i<10000; i++) {
    pair=divisors(i);
    if (i==divisors(pair)
	//	&& pair==divisors(i)
	&& i!=pair
	&& i < 10000
	&& pair < 10000) {
      sum+=i+pair;
      cout << i << " " << pair << endl;	  
    }

    
  }

  cout << sum/2 << endl;
  return 0;
}
