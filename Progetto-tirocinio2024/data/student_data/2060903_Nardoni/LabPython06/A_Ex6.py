numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
i=18
cond=True
while(cond):
    nT1=numeroTerrestre
    res=""
    while(nT1!=0):
        res+=str(nT1%i)
        nT1=nT1//i
    res=res[::-1]
    if(res==numeraleAlieno):
        print("Gli alieni hanno", i, "dita \n")
        break
    else:
        i+=1
