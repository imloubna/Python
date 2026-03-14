name=['Sri','Gill','Hari','Saran','Madhu']
age=[40,28,62,41,18]
location=['PONDY','CHENNAI','MADURAI','SALEM','TRICHY']
res=list(zip(age,name,location))
res2=sorted(res)
for i in range(5):
    print("{}.{} age is {} lives in {}". format(i+1,res2[i][1],res2[i][0],res2[i][2]))
