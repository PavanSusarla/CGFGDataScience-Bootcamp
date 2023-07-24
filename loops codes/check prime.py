#Given an integer n check if n is prime or not.
#A prime number is a number that is divisible by 1 and itself only.
def prime(n):
    count=0
    for i in range(2,n+1):
        if n%i==0:
            count+=1
    if count==1:
        return True
    else:
        return False
n=int(input())
print(prime(n))
x=0
while x<100:
    x+=2
print(x)
