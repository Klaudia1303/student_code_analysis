s1=input("immetti stringa: ")
s2=input("immetti stringa: ")
n=int(input("immetti n: "))
output=""
for i in range(len(s1)):
    if i>=n and s2[i-n:i+n+1].find(s1[i])!=-1:
        output=output+s1[i]
    elif i<n and s2[0:i+n+1].find(s1[i])!=-1:
        output=output+s1[i]
print(output)
