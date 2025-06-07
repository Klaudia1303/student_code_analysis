s1 = input("inserisci una stringa: ")
s2 = input("inserisci un'altra stringa: ")

stringaLunga = ""

for i in range(len(s1)):
    stringaRipetuta = ""
    for j in range(len(s1) - i):
        if (stringaRipetuta + s1[i + j]) in s2:
            stringaRipetuta += s1[i + j]
        else:
            break
    if len(stringaRipetuta) >=  len(stringaLunga):
        stringaLunga = stringaRipetuta

print(stringaLunga)
    
