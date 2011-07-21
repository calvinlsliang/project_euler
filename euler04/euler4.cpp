// euler4.cpp
#include <iostream>
using namespace std;

char* itoc(int n)
{
  char buffer[7];
  sprintf(buffer, "%d", n);
  return strcpy((char*) malloc(strlen(buffer)+1), buffer);
}

bool palinCheck(char n[])
{
  //  cout << n[1] << " " << n[5] << endl;
  if ((n[0] == n[5]) && (n[1] == n[4]) && (n[2] == n[3])) {
	return true;
  }
  return false;
}

int stoi(const char *c)
{
  return atoi(c);
}

int main() {
  int palin=0, num1, num2, product;
  char *temp;

  for (int i=500; i<1000; i++) {
    for (int j=500; j<1000; j++) {
      temp=itoc(i*j);
      if (palinCheck(temp)) {
	product = stoi(temp);
	if (product > palin) {
	  palin = product;
	  num1=i;
	  num2=j;
	}
      }
    }
  }

  cout << num1 << " " << num2 << endl;
  cout << palin << endl;
  return 0;
}
