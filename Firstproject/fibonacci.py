def fibb():
    a=0
    b=1
    while True:
        yield a
        # print(a)
        net=a+b
        a=b
        b=net

a=iter(fibb())

for i in range(20):
    print(next(a))



