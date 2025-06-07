numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=int(9510990939794952322311710154344301747012051743844839)
n=int(1)
while numeroTerrestre%n!=5 or (numeroTerrestre//n)%n==5:
    n=n+1
if numeroTerrestre%n==5 and (numeroTerrestre//n)%n==5:
    print(n)
