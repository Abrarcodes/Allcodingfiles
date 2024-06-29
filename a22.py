def count_4(nums):
    count =0
    
    for i in nums:
     if i==4:
            count =count +1
    return count
        
print(count_4([1,2,3,4]))
print(count_4([1,4,4,4]))
print(count_4([24,4,3,4]))