numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
resto=''
for i in range(11,100,1):
    numero = numeroTerrestre
    resto = '' 
    while  numeroTerrestre // i != 0:
        resto += str(numero % i)
        numero = numero // i
        if numero == 0:
            break
    resto = resto[::-1]
    if resto == str(numeraleAlieno):
        break
    
    else:
        continue
    
print ('Gli Alieni hanno',i,'dita')
            
        
        
        
        
        

        
        
    
        

    
    
    
    
    
