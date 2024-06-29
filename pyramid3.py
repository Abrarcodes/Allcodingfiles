rows=int(input("enter the number"))
ascii_value =65
for i in range(rows):
    for j in range(i+1):
        alphabet=chr(ascii_value)
        print(alphabet, end="")
    ascii_value+=1
    print()    