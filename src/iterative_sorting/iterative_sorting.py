# TO-DO: Complete the selection_sort() function below 

"""
UNDERSTAND:

We need to look through the array and find the smallest number
Then swap that number with the i[0] in the array,
Then we need to look from i[1] to range(len(array) - 1) to find smallest
Then swap that number with the i[1] in array.
Continue until you reach i(len(array) - 1)
"""


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp


    return arr


"""
UNDERSTAND:

We need to look at the first two items in an array i[0] and i[1],
Determine if 0 is greater than 1.
If it is, swap the place of 0 and 1.
Then move on to new i[1] and i[2].
Repeat the process until you repeat for i[-2] and i[-1]
If any places were swapped, go to the beginning of the array and 
repeat the whole process.
Return the new array

PLAN:

EXECUTE:

REFLECT:
"""

bubble_arr = [3, 2, 4, 3, 6, 8, 7, 3]
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Need a swap_occured = True
    swap_occured = True
    # While swap_occured
    while swap_occured == True:
        # For all elements from index i=0 to i=len(arr)-2
        swap_count = 0
        for i in range(len(arr) - 1):
            # Setting variables to hold numbers in index
            left_i = arr[i]
            right_i = arr[i+1]
            # if i> i+1
            if left_i > right_i:
                # Swapping values 
                arr[i] = right_i
                arr[i+1] = left_i
                # Increasing swap count
                # This will determine if while loop continues
                swap_count += 1
                # print(swap_count)
        # If no swaps occured, the loop ends. and it's sorted
        if swap_count == 0:
            swap_occured = False
    return arr

bubble_sort(bubble_arr)

print(bubble_arr)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr