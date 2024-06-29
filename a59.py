print("enter your height")
h_ft=int(input("feet"))
h_inch=int(input("inch"))
h_inch+=h_ft*12
h_cm=round(h_inch*2.54)
print(h_cm)