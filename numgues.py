import random,math
print('WELCOME TO THE NUMBER GUESSING GAME')
print("choose a number which ranges from 0 to 10")
r=random.randrange(0,11)

count=0
while  count < math.log(r + 1, 2):
    count += 1
    x=int(input('guess the number'))
    if x == r:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x < r:
        print("You guessed too small!")
    elif x > r:
        print("You Guessed too high!")
   
if count >= math.log(r + 1, 2):
    print("\nThe number is %d" % r)
    print("\tBetter Luck Next time!")
    

