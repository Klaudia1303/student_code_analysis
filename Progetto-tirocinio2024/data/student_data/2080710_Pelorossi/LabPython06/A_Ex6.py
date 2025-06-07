numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
for i in range(11,100):
    x=numeroTerrestre
    tot=''
    while x>0:
        d=x//i
        tot+=str(x%i)
        x=d
    if tot[::-1]==numeraleAlieno:
        dita=i
        break
print('le dita degli alieni sono:',dita)
        
