a = int(input())
b = int(input())
c = int(input())
if (a*b == c) and (a/b == c):
    print("2 - yes, 5 - yes")
elif (a*b == c) and not (a/b == c):
    print ("2 - yes, 5 - no")
elif not (a*b == c) and (a/b == c):
    print ("2 - no, 5 - yes")
else:
    print ("2 - no, 5 - no")
