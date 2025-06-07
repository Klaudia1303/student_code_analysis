numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

valoreConvertito = ""

i = 2

while valoreConvertito[::-1] != numeraleAlieno:
    midVal = numeroTerrestre
    while midVal > 1:
        valoreConvertito += str(midVal % i)
        midVal = midVal // i
        #print(midVal)
    
    if valoreConvertito[::-1] == numeraleAlieno:
    	continue
    
    valoreConvertito = ""
    
    i += 1

print("Gli alieni hanno", i, "dita.")