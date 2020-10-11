"""
Shell sort

Shell Sort involves sorting elements which are away from ech other.
We sort a large sublist of a given list and go on reducing the size of the list until all elements are sorted. 
The below program finds the gap by equating it to half of the length of the list size and then starts sorting all elements in it. 
Then we keep resetting the gap until the entire list is sorted.

"""


"""
procedure shellSort()
   A : array of items 
    
   /* calculate interval*/
   while interval < A.length /3 do:
      interval = interval * 3 + 1        
   end while
   
   while interval > 0 do:

      for outer = interval; outer < A.length; outer ++ do:

      /* select value to be inserted */
      valueToInsert = A[outer]
      inner = outer;

         /shift element towards right/
         while inner > interval -1 && A[inner - interval] >= valueToInsert do:
            A[inner] = A[inner - interval]
            inner = inner - interval
         end while

      /* insert the number at hole position */
      A[inner] = valueToInsert

      end for

   /* calculate interval*/
   interval = (interval -1) /3;      

   end while
   
end procedure
"""

#Algorithm shellsort
def shellSort(input_list):
    
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
# Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp

# Reduce the gap for the next element

        gap = gap//2

unsorted_list = []
num= int(input("Enter number of elements"))
print(f'Enter {num} elements')
for i in range(num):
      data = int(input(f'{i+1}. '))
      unsorted_list.append(data)
print(f 'Unsorted list is{unsorted_list}')
insertion_sort(list)
print(f'Sorted list is {shellSort(unsorted_list)}')
