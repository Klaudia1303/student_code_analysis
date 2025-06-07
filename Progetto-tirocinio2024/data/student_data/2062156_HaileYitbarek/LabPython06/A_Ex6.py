a='349776123345679876543234567876543234569055'
t=9510990939794952322311710154344301747012051743844839
for i in range(11,len(a)):
    n=0
    for j in range(len(a)):
        n=n+int(a[len(a)-1-j])*pow(i,j)
    if n==t:
        break
print('il numero delle dita degli alieni= ',i)
    
