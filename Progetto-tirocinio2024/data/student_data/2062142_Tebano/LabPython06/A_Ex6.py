u=int(input('numero in base 10='))
a=str(input('numero in base aliena='))
potenza=len(a)-1
equazione=0
P=False
m=2
while P==False:
    equazione=0
    for i in range(0,len(a)):
        equazione=equazione+int(a[i])*m**(potenza-i)
    if equazione==u:
        P=True
        print('dita alieni=',m)
    m=m+1
##numeraleAlieno="349776123345679876543234567876543234569055"
##numeroTerrestre=9510990939794952322311710154344301747012051743844839
    

        
    
      
