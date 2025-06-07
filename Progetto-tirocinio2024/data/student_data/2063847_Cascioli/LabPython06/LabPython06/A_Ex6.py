numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
cond=True
i=1
while(cond):
    nT1=numeroTerrestre
    res=''
    while(nT1!=0):
        res+=str(nT1%i)
        nt1=nT1//i
    res=res[::-1]
    if(res==numeraleAlieno):
        print("Gli alieni hanno",i,"dita")
        break
    else:
        i+=1
