s1=0
s2=0

for i in range (1,1001):
    s1+= 20
    s2+=i
    if s1==s2:
        break
    
print(i)
