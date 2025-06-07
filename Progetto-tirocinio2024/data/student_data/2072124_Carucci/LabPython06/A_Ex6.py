numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

trovato = False
i = 2
while not trovato:
        s =''
        x = numeroTerrestre
        while x>0:
            s += str(x%i)
            x //= i

        if s[::-1]==numeraleAlieno:
            trovato = True
        else:
            i+=1
print(i)
