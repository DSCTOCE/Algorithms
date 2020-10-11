#Selection Sort Algorithm
#Selection sort is an algorithm that selects the smallest element from an
#unsorted list in each iteration and places that element at the beginning of the unsorted list.

#pseudo code
      #selectionSort(array, size)
      #  repeat (size - 1) times
      #  set the first unsorted element as the minimum
      # for each of the unsorted elements
      #   if element < currentMinimum
      #     set element as new minimum
      # swap minimum with first unsorted position
      #end selectionSort

#algorithm
# Selection sort in Python


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
