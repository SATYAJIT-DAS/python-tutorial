print("\t\t\t left side\n")
for i in range(1,11):
	for j in range(i):
		print(i,end=" ")
	print("\n")

print("\t\t\t bottom up \n")

for i in range(1,11):
	for j in range(11-i):
		print(i,end=" ")
	print("\n")	


print("\t\t\t right side \n")
for i in range(1,11):
	for j in range(11-i):
		print(" ",end=" ")
	for j in range(1,i):
		print(j,end=" ")
	print("\n")		

print("\t\t\t right side top down \n")

for i in range(1,11):
	for j in range(1,i):
		print(" ",end=" ")	
	for j in range(11-i):
		print(i,end=" ")	
	print("\n")		