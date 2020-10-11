#include<bits/stdc++.h>

int main(){
  int s= 1;
  int e=n-1;
  string = word;

  printf("Please enter the string to test pallindrome");
  strings(string,n,e);
}


bool strings(str string,int s,int e)
{
  if (s==e) return true;
  if (string[s]!=string[e]) return false;
  else{
    return strings(string,s+1,e-1);
 
  }
}
