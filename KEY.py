input1 = int(input("Enter num1: "))
input2 = int(input("Enter num2: "))
input3 = int(input("Enter num3:"))


d1 = [int(d) for d in str(input1)]
d2 = [int(d) for d in str(input2)]
d3 = [int(d) for d in str(input3)]

max_sum = max(d1) + max(d2) + max(d3)

min_sum = min(d1) + min(d2) + min(d3)

key = max_sum * min_sum
print("Key =", key)
    

   
    




    