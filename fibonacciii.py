n=10
a=0
b=1
c=b
count=1
while count <=n:
    print(c)
    count+=1
    a,b=b,c
    c=a+b
    print()
      