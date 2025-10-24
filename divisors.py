#All divisors of a natural number

n = int(input("Enter Num:"))


for i in range(1,n):
    if n % i == 0:
        print(i)
print(n)