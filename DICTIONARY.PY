a = input("Enter String:")

d = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
    'E': 10000,
}

total = 0

for i in a:
    if (i in d.keys()):        
        total += d[i] 

print(total)