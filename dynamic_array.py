import sys # provides getsizeof function
data = [ ]
for k in range(20): # NOTE: must fix choice of n
	a = len(data) # number of elements
	b = sys.getsizeof(data) # actual size in bytes
	c=hex(id(data))
	print( "Length: {0:3d}; Size in bytes: {1:4d} Memory :  {2}" .format(a, b,c))
	data.append(None)