def prime(x):
    if(x==1):
        return
    i=2
    while(x%i!=0):
        i=i+1 
    print(i,end=" ")
    prime (x // i)
    
        

x = int(input("Enter any number: "))
prime(x)