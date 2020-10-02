#include<bits/stdc++.h>

using namespace std;
int sums(int n)
{
  if (n<10) return n;
  return sums(n/10)+(n%10);
}

int main()
{
  int n,a;
  cout<<"Enter the digit to find the sum"<<"";
  cin>>n;

  a = sums(n);
  std::cout << "The answer is :" << a <<'\n';
}
