#Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2.
def difference(n1, n2):
    for i in range(1, 11):
        print(n1 * i - n2 * i, end=' ')
difference(25,10)

