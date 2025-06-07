s1 = input("Inserire una striga non vuota:")
s2 = input("Inserire una striga non vuota:")

result = ""

for x in range(0, len(s1)):
    resultTemporaneo = ""
    z = x
    
    for y in range(0, len(s2)):
        if z > len(s1)-1:
            break
        if s1[z] == s2[y]:
            resultTemporaneo += s1[z]
            z += 1
            
        if (len(resultTemporaneo) > len(result)):
            result = resultTemporaneo

print(result)
