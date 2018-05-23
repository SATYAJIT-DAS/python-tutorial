def merge_sort(alist):
	lenght= len(alist)

	if lenght>1:
		mid=lenght// 2

		lefthalf= alist[:mid]
		righthalf=alist[mid:]

		merge_sort(lefthalf)
		merge_sort(righthalf)

		i,j,k=0,0,0

		while i<len(lefthalf) and j<len(righthalf) :

			pass

