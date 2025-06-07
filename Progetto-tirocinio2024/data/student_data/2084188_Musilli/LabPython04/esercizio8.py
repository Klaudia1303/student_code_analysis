s1=input("Inserire una stringa\
 (il programma termina quando l'ultimo carattere della stringa precedente è \
 al primo carattere della striga successiva): ")
b=True
while b:
    s=input("Inserire una stringa: ")
    if s1[len(s1)-1]==s[0]: b=False;
    else:   s1=s
print("\nUltime stringhe inserite:\n",s1,s)
