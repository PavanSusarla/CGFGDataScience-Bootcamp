#Given an integer s. Write a program to print the Right angle triangle wall. The length of perpendicular and base is s.  Use single loop and string multiplication.
def triangleWall(s):
    for i in range(1, s + 1):
        print("* " * i, end="\n")
s=int(input())
triangleWall(s)