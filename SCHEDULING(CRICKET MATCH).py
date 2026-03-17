import random
n=int(input("Enter num of teams:"))
teams=[]
for i in range(n):
    x=input("Enter team:")
    teams.append(x)
meet=int(input("Enter num of meeting bw two teams:"))
matches=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            matches.append([teams[i],teams[j]])
random.shuffle(matches)
pos=1
for i in matches:
    print("Match {}: {} vs {}". format(pos,i[0],i[1]))
    pos=pos+1