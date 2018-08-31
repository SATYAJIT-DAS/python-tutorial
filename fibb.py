from time import time
# fibb_cache={}
# def fibb(n):
# 	if n in fibb_cache:
# 		return fibb_cache[n]
# 	if n==1:
# 		value=1
# 	elif n==2:
# 		value=1
# 	elif n>2:
# 		value=fibb(n-1)+fibb(n-2)
# 	fibb_cache[n]=value
# 	return value

# start = time()
# for n in range(1,10):
# 	print(fibb(n))

# end=time()

# print(end-start)

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibb(n):
	if n==1:
		return 1
	elif n==2:
		return 1
	elif n>2:
		return fibb(n-1)+fibb(n-2)
	
start = time()
for n in range(1,10):
	print(fibb(n))

end=time()

print(end-start)

