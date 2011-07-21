// euler34.cpp
#include <iostream>
#include <iomanip>
using namespace std;

int factorial(int n) 
{
  int product=1;
  for (int i=1; i<=n; i++) {
    product*=i;
  }
  return product;
}

char* itoc(int n) 
{
  char buffer[15];
  string s;
  sprintf(buffer, "%d", n);
  return strcpy((char*) malloc(strlen(buffer)+1), buffer);
}

int stoi(char c) 
{
  char b[2];
  b[0]=c;
  b[1]='\0';
  return atoi(b);
}

int sumFact(int n)
{
  int sum=0;
  char *temp=itoc(n);
  int i=0;
  while (temp[i] != '\0') {
    sum+=factorial(stoi(temp[i]));
    i++;
  }
  return sum;
}

bool equalFact(int n) {
  return (n==sumFact(n));
}

int main(void) {
  int sum=0;
  for (int i=1; i<3000000; i++) {
    if (equalFact(i)) {
      sum+=i;
    }
  }
  cout << sum << endl;
  return 0;
}
