numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

x = 10
while True:
    conv = 0
    for i in range(len(numeraleAlieno)):
        pos = len(numeraleAlieno) - 1 - i
        cifra = ord(numeraleAlieno[i]) - ord("0")
        conv += cifra * (x ** pos)
    if conv == numeroTerrestre:
        print(x)
        break
    x += 1
