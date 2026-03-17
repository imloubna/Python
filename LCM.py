a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
l=max([a,b])
s=min([a,b])
step = l

while True:
    if (l%s==0):
        break
    else:
        l=l+step
print("LCM:", l)