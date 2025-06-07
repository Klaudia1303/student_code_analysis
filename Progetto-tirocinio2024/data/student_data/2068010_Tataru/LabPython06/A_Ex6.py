numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
ntt=numeroTerrestre
nat=""
con=False
i=2
while (con==False):
    if(ntt==0):
        nat=nat[::-1]
        if(nat==numeraleAlieno):
            print(i)
            break
        else:
            nat=""
            ntt=numeroTerrestre
            i+=1
            continue
    nat=nat+str(ntt%i)
    ntt=ntt//i

