#Program to check if a number is Positive, Negative, Odd, Even, Zero

n = int(input("Enter Num: "))

def posNeg(x):
    if x >= 0:
        return True
    return False
def oddEven(x):
    if x % 2 == 0:
        return True
    return False

if posNeg(n) and oddEven(n):
    print(n,"Positive and Even")
elif posNeg(n) and  not oddEven(n):
    print(n,"Positive and Odd")
elif not posNeg(n) and   oddEven(n):
    print(n,"Negative and Even")
else:
   print(n,"Negative and Odd")






