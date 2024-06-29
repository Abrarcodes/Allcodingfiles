def num(a,b,c):
    if (a==b or b==c or c==a):
        return 0
    else:
        return a+b+c
    
print(num(1,2,3))
print(num(12,32,43))
print(num(1,1,3))