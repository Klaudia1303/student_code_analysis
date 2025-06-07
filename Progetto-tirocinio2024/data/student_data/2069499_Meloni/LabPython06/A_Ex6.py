numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

numal=int(numeraleAlieno)
base=11
somma=0
while base>10:
    esp=0
    pos=-1
    while esp<len(numeraleAlieno) and pos>(-1*len(numeraleAlieno)-1):
        somma+=(int(numeraleAlieno[pos]))*(base**esp)
#        print(esp, somma)
        esp+=1
        pos-=1
    if somma!=numeroTerrestre:
        base+=1
        somma=0
#        print('Attenzione la base è stata aumentata a ',base)
    else:
        print(base)
        base=0
        
