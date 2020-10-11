#BUBBLESORT Algorithm
#Bubble sort is an algorithm that compares the adjacent elements and swaps their positions if they are not in the intended order.
#The order can be ascending or descending.

#pseudocode

#bubbleSort(array)
#  for i <- 1 to indexOfLastUnsortedElement-1
#    if leftElement > rightElement
#      swap leftElement and rightElement
#end bubbleSort

#Algorithm
def bubbleSort(array):
    
    # run loops two times: one for walking throught the array 
    # and the other for comparison
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):

            # To sort in descending order, change > to < in this line.
            if array[j] > array[j + 1]:
                
                # swap if greater is at the rear position
                (array[j], array[j + 1]) = (array[j + 1], array[j])


data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print('Sorted Array in Asc ending Order:')
print(data)
