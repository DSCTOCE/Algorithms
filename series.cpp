#include<bits/stdc++.h>

void series(int n){
  if (n==0){
    return;
  }
  else{
    std::cout<<n<<""<<"\n";
    series(n-1); 
  }
}

int main(){
  int n;
  std::cout << "Please enter the value of n" << '\n';
  scanf("%d\n",&n );
  series(n);
}
