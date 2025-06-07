s1 = str(input('Insert string: '))
s2 = str(input('Insert string: '))
n = int(input('Insert number: '))
ns=''
for i in range(len(s1)):
    ps = s2.find(s1[i])
    if ps==-1:
        continue
    elif ps-i<=n and i-ps<=n:
        ns=str(ns)+str(s1[i])
print(ns)
