numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre="9510990939794952322311710154344301747012051743844839"
x=10
numTA=0
while numTA!=int(numeraleAlieno):
    x+=1
    numTA=0
    div=int(numeroTerrestre)
    exp=0
    while div!=0:
        numTA+=(div%x)*(10**exp)
        div=div//x
        exp+=1
print (x)
