#Given an integer S, write a program to print the square of size S using * character.
def square(s):
    for i in range(1,s+1):
        for j in range(1,s+1):
            if i==1 or i==s or j==1 or j==s:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
s=int(input())
square(s)