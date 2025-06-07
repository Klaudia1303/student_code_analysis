s=input('Inserire una stringa:')
piùdiuna=False
for i in range (len(s)):
    if s[i] in s[i+1:]:
        piùdiuna=True
print(piùdiuna)
    
    

