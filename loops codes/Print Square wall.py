#Given an integer s,  write a program to print the square wall of size s using single loops. Use * character to make the wall.
def squareWall(s):
    # Complete the below code
    # Replace .... by your own code
    for i in range(s):
        for j in range(s):
            print("*", end=" ")
        print()
s=int(input())
squareWall(s)