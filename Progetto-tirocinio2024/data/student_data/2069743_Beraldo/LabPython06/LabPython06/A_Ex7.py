s1 = input("Inserire prima stringa: ")
s2 = input("Inserire seconda stringa: ")
m = 0
posf = 0
posi = 0
for i in range(len(s2)):
    for j in range(i+1,len(s2)):
        if s2[i:j] in s1 and len(s2[i:j]) >= m:
            m = len(s2[i:j])
            posi = i
            posf = j
print(s2[posi:posf])
            
