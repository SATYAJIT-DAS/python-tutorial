def binary_search(alist,left,right,target):
	# if left>right:
	# 	return False
	if right>=left:
		mid=left+right//2
		if target==alist[mid]:
			return mid #return the index
		elif target < alist[mid]:
			return binary_search(alist,left,mid-1,target)
		else:
			return	binary_search(alist,mid+1,right,target)
	else:
		return -1


alist=[1,2,5,36,9,69,59,6,58,26,25,56,15]
result=binary_search(alist,0,len(alist),19)
if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array")

			