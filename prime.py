import time
# import math
def isPrimeV1(n):
	"""if n is prime return true else false"""
	if n==1:
		return False
	for d in range(2,n):
		if n%d==0:
			return False
	return True
		
t0= time.time()
for i in range(1,101):
	 print(i ,isPrimeV1(i))
	#isPrimeV1(i)

t1= time.time()

print ("time diff :", t1-t0)

# def isPrimeV2(n):
# 	if n==1:
# 		return False
# 	divisor= math.floor(math.sqrt(n))
# 	for d in range(2,1+divisor):
# 		if n%d==0:
# 			return False
# 	return True	

# t0= time.time()
# for i in range(1,100001):
# 	print(i ,isPrimeV2(i))
# 	isPrimeV2(i)
# t1= time.time()

# print ("time diff :", t1-t0)

# def isPrimeV3(n):
# 	if n==1:
# 		return False
# 	if n==2:
# 		return True
# 	if n%2==0:
# 		return False

# 	max_divisor= math.floor(math.sqrt(n))
# 	for d in range(3,1+max_divisor,2):
# 		if n%d ==0:
# 			return False
# 	return True		  			

# t0= time.time()
# for i in range(1,100001):
# 	# print(i ,isPrimeV3(i))
# 	isPrimeV3(i)
# t1= time.time()

# print ("time diff :", t1-t0)