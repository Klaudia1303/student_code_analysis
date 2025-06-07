s1 = input("Inserire prima stringa: ")
s2 = input("Inserire seconda stringa: ")
x = 0
F = 0
I = 0
for i in range(len(s2+1)):
    for j in range(i+1,len(s2+1)):
        if s2[i:j] in s1 and len(s2[i:j]) >= x:
            x = len(s2[i:j])
            I = i
            F = j
print(s2[I:F])
