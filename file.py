fp= open('filetestw.txt', 'w+')
reply= input("enter x and y separeted by spaces: ")
pieces= reply.split()
x=float(pieces[0]);
y=float(pieces[1]);
total=sum([x,y])
fp.write("sum of x and y is :%d\r\n"%total)
fp.close()
fp=open('filetest.txt','r')
print(fp.read())
fp.close()