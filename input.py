reply= input("enter numbers separeted by spaces: ")
pieces= reply.split()
# x=float(pieces[0])
# y= float(pieces[1])

alist=list()

for j in range(len(pieces)):
	alist.append(float(pieces[j]))

print("sum of x and y  ",sum(alist))