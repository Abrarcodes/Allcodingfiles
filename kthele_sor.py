
def ksmall (arr,k):
    arr_sorted=sorted(arr)
    return arr_sorted[k-1]
    
def k_large(arr,k):
    arr_sorted=sorted(arr)
    return arr_sorted[-k]
    
arr=[1,2,3,4,5,6,7,8,9,0]
k=4
print("min is ", ksmall(arr,k))
print("max is ", k_large(arr,k))
