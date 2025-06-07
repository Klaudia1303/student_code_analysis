b=True
while b:
    s=str(input("Inserire  una stringa (il programma termina quando la stringa\
 è composta da caratteri alfabetici minuscoli o da una stringa con spazi): "))
    print(s[0]+s[len(s)-1])
    if s.isalpha() and s.islower(): b=False
