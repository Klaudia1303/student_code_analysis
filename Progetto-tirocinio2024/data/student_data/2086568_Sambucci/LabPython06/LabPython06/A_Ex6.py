numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
corretto=False
b=2
while not corretto:
    nTA=''
    d=numeroTerrestre
    while d!=0:
        nTA=nTA+str(d%b)
        d=d//b
    if nTA[::-1]==numeraleAlieno:
        corretto=True
        print('La base extratterestre è',b)
    else:
        b+=1
print('Gli extratterrestri hanno',b,'dita')
        
        
    
    
    

