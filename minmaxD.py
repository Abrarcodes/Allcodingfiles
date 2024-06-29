#for searching in an array
def getmin(arr,n):
    res=arr[0]
    for i in range(1,n):
        res=min(res,arr[i])
    return res

def getmax(arr,n):
    res=arr[0]
    for i in range(1,n):
        res=max(res,arr[i])
    return res

arr=[23,42,53,5,3,2,1]
n=len(arr)
print("minimum array is ", getmin(arr,n))
print("maximum array is ", getmax(arr,n))