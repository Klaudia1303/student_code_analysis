s1 = input ("inserire la stringa s1: ")
s2 = input ("inserire la stringa s2: ")
a=""
b=""
for i in range (0, len(s1)):
    for j in range (0, len(s2)):
        if s1[i] == s2[j]:
            b=""
            for x in range (0,len(s2)-j):
                if s1[x+i]==s2[x+j]:
                    b = b +s1[i+x]
                else:
                    break
            if len(b) > len(a):
                a = b
print (a)
        
            


 
            
