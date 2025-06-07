numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839
num2=numeroTerrestre
num=""
i=2
while num!=int(numeraleAlieno):
    num2=numeroTerrestre
    num=""
    while num2>i:
        num2=num2//i
        num=str(num2%i)+num
    i+=1
print(num)
