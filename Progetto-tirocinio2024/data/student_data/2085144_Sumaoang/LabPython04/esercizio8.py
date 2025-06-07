i = 0
s1 = input("Inserire una stringa:") #s1: ultima stringa
s2 = input("Inserire una stringa:") #s2: attuale stringa

while s1[len(s1)-1] != s2[0]:
    s1 = s2
    s2 = input("Inserire una stringa:")
print(s1 + " " + s2)
    
    
