alist=[1,2,1,3]
large_index=0;

for j in range(len(alist)):
	if alist[j]>alist[large_index]:
		large_index=j

print('largest number in list is ',large_index,'.')		
val= max(alist)
print(val)
print(sorted(alist))
print(sum(alist))
print(type(alist))
