#include <bits/stdc++.h>
using namespace std;

class Node{
public:
  int data;
  Node* next;
};

//Program to traversal the linked list
void print_trav(Node* n)
{
  while (n!=NULL) {
    std::cout << n->data << '\n';
    n=n->next;
  }
}

int main(){
  Node* head = NULL;
  Node* second = NULL;
  Node* third = NULL;

  //Allocating three nodes for heaps
  head = new Node();
  second = new Node();
  third = new Node();

  head->data=1;
  head->next = second;

  second -> data=2;
  second ->next = third;

  third -> data = 3;
  third->next= NULL;


  print_trav(head);
  return 0;
}
