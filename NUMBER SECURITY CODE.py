a = input("Enter security code: ")
a=[int(i) for i in str(a)]
b=[]
for i in a:
    if i not in b:
        b.append(i)
count=0
for i in b:
    if a.count(i)>1:
        count=count+1
print(count)