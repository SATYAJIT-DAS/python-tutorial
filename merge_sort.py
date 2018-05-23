def merge_sort(alist):
	print("Splitting ",alist)
	if len(alist)>1:
		mid= len(alist)//2
		lefthalf= alist[:mid]
		righthalf=alist[mid:]

		merge_sort(lefthalf)
		merge_sort(righthalf)

		i,j,k=0,0,0

		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i]>righthalf[j]:
				alist[k]=righthalf[j]
				j=j+1
			elif lefthalf[i]<righthalf[j]:
				alist[k]=lefthalf[i]
				i=i+1
			k =k+1

		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
	print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)	
			

				
			