"""
Insertion sort


Insertion sort involves finding the right place for a given element in a sorted list. So in beginning we compare the first two elements 
and sort them by comparing them. Then we pick the third element and find its proper position among the previous two sorted elements. 
This way we gradually go on adding more elements to the already sorted list by putting them in their proper position.

"""
"""
pseudo code

procedure insertionSort( A : array of items )
int holePosition
   int valueToInsert
	
   for i = 1 to length(A) inclusive do:
	
      /* select value to be inserted */
      valueToInsert = A[i]
      holePosition = i
      
      /*locate hole position for the element to be inserted */
		
      while holePosition > 0 and A[holePosition-1] > valueToInsert do:
         A[holePosition] = A[holePosition-1]
         holePosition = holePosition -1
      end while
		
      /* insert the number at hole position */
      A[holePosition] = valueToInsert
      
   end for
	
end procedure
"""
#Algorithm
def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element

unsorted_list = []
num= int(input("Enter number of elements"))

print(f'Enter {num} elements')

 for i in range(num):
      data = int(input(f'{i+1}. '))
      unsorted_list.append(data)
print(f 'Unsorted list is{unsorted_list}')
insertion_sort(list)
print(f'Sorted list is {merge_sort(unsorted_list)}')
