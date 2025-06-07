nA="349776123345679876543234567876543234569055"
nT=9510990939794952322311710154344301747012051743844839
for i in range(11, len(nA)):
    n = 0
    for j in range(len(nA)):
        n += int(nA[len(nA)-1-j])*pow(i,j)
    if n == nT:
        break
print(i)
