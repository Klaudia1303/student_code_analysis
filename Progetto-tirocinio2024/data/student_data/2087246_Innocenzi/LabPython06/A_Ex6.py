numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
k=True
x=10
while(k):
    n_10=numeroTerrestre
    n_alieno=''
    while(n_10!=0):
        resto=n_10%x
        n_10=n_10//x
        n_alieno+=str(resto)
    if (n_alieno[::-1]==numeraleAlieno):
        print(x)
        break
    x+=1


    