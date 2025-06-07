numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
for i in range(11,100):
    x=numeroTerrestre
    resto=""
    while x>0:
        divisione=x//i
        resto+=str(x%i)
        x=divisione
    if resto[::-1]==numeraleAlieno:
        dita=i
        break
print("Gli alieni hanno",dita, "dita")
