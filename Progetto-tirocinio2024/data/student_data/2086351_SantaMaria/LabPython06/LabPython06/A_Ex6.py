alieno = "349776123345679876543234567876543234569055"
umano = "9510990939794952322311710154344301747012051743844839"
potenza = len(alieno) - 1
for i in range(11,30):
    codifica = 0
    for k in range(potenza, 0):
        codifica = codifica + int(alieno[k]) * (i ** k)
    if str(codifica) == umano:
        print("La base è "+i)
        break
