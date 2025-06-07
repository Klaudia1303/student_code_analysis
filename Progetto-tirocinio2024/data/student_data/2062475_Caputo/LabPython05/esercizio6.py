s = input ("inserire la stringa s: ")
massimo = 0
for i in range (0, len(s)):
    if s.rfind(s[i]) > massimo:
        massimo = s.rfind(s[i])
        distanza = s.rfind(s[i]) - i
print ("la distanza massima tra due caratteri uguali è:", distanza)
    
    
