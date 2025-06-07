s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una stringa: ")
lmax = 0
smax = ''
if len(s1) !=0 and len(s2) != 0:
    for i in range(len(s1)):
        for j in range(i+1,len(s1)+1):
            s = s1[i:j]
            if s in s2:
                l = j-i
                if l >= lmax:
                    lmax = l
                    smax = s
            else:
                break
print(smax)
            

    
