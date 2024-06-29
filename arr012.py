arr=[1,0,0,0,1,1,1,1,1,0,2,2,2,2,0,2]
print(len(arr))
a=0
b=0
c=len(arr)-1

while b <= c:
    if arr[b]==0:
        arr[a],arr[b]= arr[b],arr[a]
        a+=1
        b+=1
    elif arr[b]==1:
        b+=1
    else :
        arr[c],arr[b]= arr[b],arr[c]
        c-=1
print("sorted array is ",arr)    
    

    
