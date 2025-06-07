s1=input("Inserire la prima stringa: ")
s2=input("Inserire la seconda stringa: ")
lun_s1=len(s1)
lun_s2=len(s2)
pre = " "
j = 0
mas = " "
for k in range(lun_s1):
    j = s2.find(s1[k])
    if j>-1:
        for j in range(j,lun_s2):
            if s1[k] == s2[j]:
                pre+=s1[k]
                k+=1
            else:
                if mas<pre:
                    mas = pre
                    pre = " "
                break
print(mas)
                    
            
