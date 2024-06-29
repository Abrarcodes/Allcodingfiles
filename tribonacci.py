n=int(input("enter the number"))
a,b,c=0,0,1
for i in range(3,n+1):
    next=a+b+c
    a,b,c=b,c,next
print(c)

    