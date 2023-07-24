#Given an integer N find the sum of the first N natural number.
def nSum(n):
    ans = 0
    for i in range(1, n + 1):
        ans += i
    return ans
n=int(input("Enter ther number"))
print(nSum(n))