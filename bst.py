# def binarySearch(alist, item):
#     first = 0
#     last = len(alist)-1
#     found = False
   
#     while first<=last and not found:
#         midpoint = (first + last)//2
#     if alist[midpoint] == item:
#         found = True
#     else:
#         if item < alist[midpoint]:
#             last = midpoint-1
#         else:
#             first = midpoint+1 
#     return found

  
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binarySearch(testlist, 3))
# print(binarySearch(testlist, 13))
def binary search(data, target, low, high):
”””Return True if target is found in indicated portion of a Python list.

 The search only considers the portion from data[low] to data[high] inclusive.
 ”””
    if low > high:
        return False # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]: # found a match
            return True
        elif target < data[mid]:
             # recur on the portion left of the middle
            return binary search(data, target, low, mid − 1)
        else:
            return binary search(data, target, mid + 1, high)
