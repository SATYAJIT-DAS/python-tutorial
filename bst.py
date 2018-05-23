def bst(alist,target):
    mid = len(alist)//2 #it will divide list into two part at this point

    if target == alist[mid] :
        return mid

    elif target < alist[mid] :
        alist=alist[:mid]
        bst(alist,target)
    elif target > alist[mid]:
        alist=alist[mid:]
        bst(alist,target)
    else:
        return "not found"

alist=[10,23,25,36,64,78,89,98]
result=bst(alist,23)
if result =="not found":
    print ("Your target is not in list")
else :
    print("your target is in {} no index of list ".format(result))
