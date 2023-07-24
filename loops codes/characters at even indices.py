#printing charecters at even indices using slicing
s = input().strip()
for i in range(0, len(s), 2):  ## from 0 to length of str and skip 2
    print(s[i], end="")
    