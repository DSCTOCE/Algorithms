//Write a program and recurrence relation to find the Fibonacci series of n where n>2 .

#include<bits/stdc++.h>

using namespace std;

int fib(int n){
  if (n==0) return 0;
  if (n==1 || n==2) return 1;

  else{
    return fib(n-1)+fib(n-2);
  }
}


int main(){
  int n,a;
  std::cout << "Enter the number to find the fibbonacci series:" << '\n';
  std::cin >> n;
  // for (int i=0;i<=n;i++){
  for (int i = 0; i < n; i++) {
        printf("%d ", fib(i));
    }
  // std::cout << a << '\n';
    // }
}
