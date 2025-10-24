#Prime Numbers
n = int(input("Enter Number : "))

def prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    for i in range(3,x):
        if x % i == 0:
            return False
    return True
if prime(n):
    print("Prime")
else:
    print("Not Prime")