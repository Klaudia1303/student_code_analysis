na="349776123345679876543234567876543234569055"
nt=9510990939794952322311710154344301747012051743844839
for i in range(11, len(na)):
    n = 0
    for j in range(len(na)):
        n += int(na[len(na)-1-j])*pow(i,j)
    if n == nt:
        break
print(i)
