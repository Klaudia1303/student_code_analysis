numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

# numero terrestre)10 = numerale alieno)x
# len numerale alieno = 42
# len numero terrestre = 52

for i in range(11, len(numeraleAlieno)):
    n = 0
    for j in range(len(numeraleAlieno)):
        n += int(numeraleAlieno[len(numeraleAlieno) - 1 -j]) * pow(i,j)
    if n == numeroTerrestre:
            break
print(i)
