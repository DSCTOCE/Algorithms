# Kadane's Algorithm finds the contiguous sub-array, within an array of integers, which has the largest sum.
# a=[-1,2,4,-3,5,2,-5,2]
# b=a.copy()
# len=len(a)
# max_sum=0
# for i in range(len):
#     sum=a[i]
#     for j in range(i+1,len):
#         sum+=a[j]
#         if sum>max_sum:
#             max_sum=sum
# print(max_sum)
# Function to find contiguous sublist with the largest sum
# in given set of integers
def kadane(A):
    # stores maximum sum sublist found so far
    maxSoFar = 0

    # stores maximum sum of sublist ending at current position
    maxEndingHere = 0

    # traverse the given list
    for i in A:
        # update maximum sum of sublist "ending" at index i (by adding
        # current element to maximum sum ending at previous index i-1)
        maxEndingHere = maxEndingHere + i

        # if maximum sum is negative, set it to 0 (which represents
        # an empty sublist)
        maxEndingHere = max(maxEndingHere, 0)

        # update result if current sublist sum is found to be greater
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxSoFar


if __name__ == '__main__':

    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("The sum of contiguous sublist with the largest sum is", kadane(A))
