#Given an integer N. Write a program to return the factorial of N.
def nFactorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans
n=int(input())
print(nFactorial(n))



