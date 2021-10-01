#include<iostream>
#include<algorithm>
#include<string>

using namespace std;


void bubbleSort(int arr[],int size);

int main(){
    int a;
    cout<<"Enter the size of array : "<<endl;
    cin>>a;
    int arr[a];
    for(int i=0;i<a;i++){
        cout<<"Enter the "<<i+1<<" th element :"<<endl;
        cin>>arr[i];
    }
    bubbleSort(arr,a);
}

void bubbleSort(int arr[],int size){
    int counter=1;
    while(counter<size){
        for(int i=0;i<size-counter;i++){
            if(arr[i]>arr[i+1]){
                int temp;
                temp=arr[i];
                arr[i]=arr[i+1];
                arr[i+1]=temp;
            }
            
    }
    counter++;
}
    cout<<"Sorted array : "<<endl;
    for(int i=0; i<size; i++){
        cout<<arr[i]<<endl;
    }
}
