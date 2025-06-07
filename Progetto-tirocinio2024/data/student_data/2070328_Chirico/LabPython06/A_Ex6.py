numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839


nT =''

b = 11


while numeraleAlieno != nT:
     n = numeroTerrestre
     nT = ''
     for i in range(len(str(n))):
         nT = str(n%b)+nT
         n = n//b
         
         
     while nT[0] == '0':
        nT = nT.replace(nT[0],'',1)
        
        
     if numeraleAlieno != nT:
         b = b+1

        

print(b)


