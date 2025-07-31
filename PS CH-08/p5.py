def ptrn(n):
    if(n==0):
        return
    print("*" * n)
    ptrn(n-1)
ptrn(3)