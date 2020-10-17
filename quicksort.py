"""
Quick sort


Like Merge Sort, QuickSort is a Divide and Conquer algorithm. 
It picks an element as pivot and partitions the given array around the picked pivot. 
"""


"""
pseudo code

function partitionFunc(left, right, pivot)
   leftPointer = left
   rightPointer = right - 1

   while True do
      while A[++leftPointer] < pivot do
         //do-nothing            
      end while
        
      while rightPointer > 0 && A[--rightPointer] > pivot do
         //do-nothing         
      end while
        
      if leftPointer >= rightPointer
         break
      else                
         swap leftPointer,rightPointer
      end if
        
   end while 
    
   swap leftPointer,right
   return leftPointer
    
end function

procedure quickSort(left, right)

   if right-left <= 0
      return
   else     
      pivot = A[right]
      partition = partitionFunc(left, right, pivot)
      quickSort(left,partition-1)
      quickSort(partition+1,right)    
   end if        
   
end procedure
"""

def partition(arr, low, high):

    i = (low-1)

    pivot = arr[high]
 

    for j in range(low, high):

        if arr[j] <=pivot:

            i = i+1

            arr[i], arr[j] = arr[j], arr[i]
 

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)
 
 
 

def quickSort(arr, low, high):

    if len(arr) == 1:

        return arr

    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)

        quickSort(arr, pi+1, high)
 


unsorted_list = []
num= int(input("Enter number of elements"))

print(f'Enter {num} elements')

for i in range(num):
      data = int(input(f'{i+1}. '))
      unsorted_list.append(data)
print(f'Unsorted list is{unsorted_list}')
quickSort(unsorted_list,0,num-1)
print(f'Sorted list is {unsorted_list'})
