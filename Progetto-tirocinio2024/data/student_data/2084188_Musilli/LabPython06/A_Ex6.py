numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

def cambiobase(numero, base):
    s=0; l=len(numero)-1
    for c in numero:
        s+=int(c)*(base**l); l-=1
    return s

b=2; t=True
while t:
    ris=cambiobase(numeraleAlieno,b)
    if ris==numeroTerrestre: print("Il numero risulta in base:",b); t=False
    b+=1
