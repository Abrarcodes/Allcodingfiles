def abc(group,n):
    for i in group:
        if n==i:
          return True
    
    return False

print(abc([1,2,3,4,5],21))
    