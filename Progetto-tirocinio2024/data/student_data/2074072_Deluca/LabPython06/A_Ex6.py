numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre="9510990939794952322311710154344301747012051743844839"
b=9
fnd=False
numeroalieno=0
while not fnd:
    numeroalieno=0
    for i in range(len(numeraleAlieno)-1,-1,-1):
        numeroalieno+=(b**i)*(int(numeraleAlieno[-1-i]))
    if str(numeroalieno)==numeroTerrestre:
        fnd=True
        print(b)
    else:
        b+=1
