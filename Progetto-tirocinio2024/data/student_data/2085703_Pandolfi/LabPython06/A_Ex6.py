numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

numeroAlieno = 0
b_aliena = 10

while numeroAlieno < numeroTerrestre:
	numeroAlieno = 0
	b_aliena += 1
	for x in range(len(numeraleAlieno)):
		numeroAlieno = int(numeraleAlieno[-x]) * (b_aliena ** x)


print(b_aliena)

