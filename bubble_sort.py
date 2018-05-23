def bubble_sort(alist):
	lenght=len(alist)

	for i in range(lenght):
		for j in range(0,lenght-1):
			if alist[j]>alist[j+1]:
				alist[j],alist[j+1]=alist[j+1],alist[j]

alist = [64, 34, 25, 12, 22, 11, 90]
 
bubble_sort(alist)
 
print ("Sorted array is:")
for i in range(len(alist)):
    print ("%d" %alist[i])



    