# -*- coding: utf-8 -*-
"""Counting-Sort.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BCnSg8CmU7nW-4iqghHUxPIOb3LlApIl
"""

def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)

    # Create a count array to store the count of each unique object
    count = [0] * (max_val + 1)

    # Store the count of each number
    for num in arr:
        count[num] += 1

    # Build the sorted output array
    sorted_index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1
            count[i] -= 1

# Example usage
if __name__ == "__main__":
    array = [4, 2, 2, 8, 3, 3, 1]

    print("Original array:")
    print(array)

    counting_sort(array)

    print("Sorted array:")
    print(array)