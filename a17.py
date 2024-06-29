def arm(n):
    return (abs(1000-n)<=100) or (abs(2000-n)<=100)
print(arm(1000))
print(arm(900))
print(arm(800))
print(arm(2200))
