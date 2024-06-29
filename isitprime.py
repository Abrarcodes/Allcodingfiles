def is_prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    for i in range(3,(n**0.5)+1,2):
        if i%2==0:
            return False
    else:
        return True
    
arr=[1,2,3,4,5,6,7]
for num in arr:
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")