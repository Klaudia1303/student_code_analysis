numeraleAlieno="349776123345679876543234567876543234569055"
numeroTerrestre=9510990939794952322311710154344301747012051743844839

result=0
current_base = 1

while True:
    accumulator=0
    power = len(numeraleAlieno) - 1
    for ch in numeraleAlieno:
        accumulator += int(ch)*current_base**power
        power -= 1

    if accumulator == numeroTerrestre:
        break
    current_base += 1
print(current_base)
