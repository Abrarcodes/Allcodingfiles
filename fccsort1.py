test_list=[21,23,43,112,223]
flag=0
test_list1=test_list[:]
test_list1.sort()
if(test_list1== test_list):
    flag=1
    
if (flag):
    print("sorted")
else:
    print("not sorted")
