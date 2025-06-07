numALIENO="349776123345679876543234567876543234569055"
numTERRA=9510990939794952322311710154344301747012051743844839
numero=0
base=10
while numero!=numTERRA:
    numero=0
    base=base+1
    for i in range(len(numALIENO)):
        numero=numero+int(numALIENO[i])*base**(len(numALIENO)-1-i)
print(base)
if numero==numTERRA:
    print(base)
