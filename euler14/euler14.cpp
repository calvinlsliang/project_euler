// euler14.cpp
#include <iostream>
using namespace std;

int main() {
  int big=1000000;
  unsigned int max_chain=0, num=0, chain, counter;
  for (int i=1; i<big; i++) {
    chain=1;
    counter=i;

    while(counter!=1) {
      if (counter<0) {
	chain=1;
	break;
      }
      if(counter%2==0) {
	counter=counter/2;
      } else {
	counter=(3*counter)+1;
      }
      chain++;
    }
    
    if (chain>=max_chain) {
      num=i;
      max_chain=chain;
    }
    //    cout<<i<<endl;
    
  }

  cout << "num: " << num << endl;
  cout << "max_chain: " << max_chain << endl;

  return 0;
}
