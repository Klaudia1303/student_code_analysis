s1 = input ('Inserisci una stringa di testo: ')
s2 = input ('Inserisci una stringa di testo: ')
n = int (input('Inserisci un numero intero: '))
fine= '' 
for i in range (len(s1)):
    if i > n and i< len(s2)-n:
        if s1[i]==s2[i+2] or s1[i]==s2[i-2]:
            fine = fine + s1[i]
            print(s1[i])
    elif i< n :
        if s1[i]==s2[i+2] :
            fine = fine + s1[i]
    elif i<len(s2)-n:
        if s1[i]==s2[i-2]:
            fine = fine + s1[i]
print(fine)
