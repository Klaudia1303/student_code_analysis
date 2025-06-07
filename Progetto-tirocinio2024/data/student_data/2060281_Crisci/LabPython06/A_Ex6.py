numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
avanti=True
base=10
numero=''
lun=len(numeraleAlieno)
for i in range(11, lun):
    n=0
    for j in range(lun):
        n=n+int(numeraleAlieno[lun-1-j])*pow(i,j)
    if n==numeroTerrestre:
            break
print(i)
