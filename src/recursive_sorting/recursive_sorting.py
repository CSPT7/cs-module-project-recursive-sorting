# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB) # TOTAL NUMBER OF 'ELEMENTS' IN COMBINED ARRAY
    merged_arr = [0] * elements  # CREATE A VARIABLE TO HOLD THE FINAL COMBINED ARRAY

    # WHILE THE ARRAYS TO BE COMPARED ARE NOT EMTPY,
    while len(arrA) > 0 and len(arrB) > 0:
        # COMPARE THE HEAD OF EACH ARRAY
        if arrA[0] <= arrB[0]:
            # IF THE HEAD OF LEFTMOST ARRAY IS SMALLER THAN THE HEAD OF RIGHTMOST ARRAY, APPEND HEAD OF LEFTMOST ARRAY INTO `merged_arr`
            merged_arr.append(arrA[0])
            # REMOVE THE CURRENT HEAD FROM THE LEFTMOST ARRAY
            arrA.pop(0)
        # IF THE HEAD OF THE LEFTMOST ARRAY IS NOT SMALLER THATN THE HEAD OF THE RIGHTMOST ARRAY, APPEND THE HEAD OF THE RIGHTMOST ARRAY INTO `merged_arr`
        else:
            merged_arr.append(arrB[0])
            # REMOVE THE CURRENT HEAD FROM THE LEFTMOST ARRAY
            arrB.pop(0)

    while len(arrA) is not 0:
        merged_arr.append(arrA[0])
        arrA.pop(0)
    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        arrB.pop(0)
    
    return merged_arr

    # REFERENCES: [Merge Sort](https://medium.com/@tuvo1106/merge-sort-in-python-5d9617fb9ee1), [Merging Two Lists](https://en.wikipedia.org/wiki/Merge_algorithm#:~:text=Conceptually%2C%20merge%20sort%20algorithm%20consists,sub%2Dlists%20of%20size%201.)


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here


    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    mid = arr() // 2

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    # RECURSIVELY BREAK UP THE ARRAY INTO 'LEFT_HALF' AND 'RIGHT_HALF' UNTIL IT IS DONW TO ONE ELEMENT
    # USE 'MERGE_IN_PLACE' TO 

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
