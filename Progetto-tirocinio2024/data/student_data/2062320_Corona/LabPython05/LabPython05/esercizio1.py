s1= (input())
s2 = (input())
p=0
for i in s1:
    print(i,end='')
    for j in s2[p]:
        print(j,end='')
        p=p+1
