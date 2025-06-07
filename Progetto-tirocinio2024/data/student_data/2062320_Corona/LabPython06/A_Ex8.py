#s1= str(input())
#s2= str(input())
s1='cestello'
s2='sportina'
n=2
ris=''


for c in s1:
    i= s1.find(c)

    if i<n:
        continue
    elif c in s2:
        ris=ris+c
    else:
        break   
print(ris)