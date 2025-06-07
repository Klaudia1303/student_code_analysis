s=input("Inserisci stringa --> ")
if len(s)>=2:
    n=int(input("Inserisci numero --> "))
    a=False
    for i in range(len(s)):
        if (i+n)<len(s):
            if s[i]==s[i+n]:
                a = True
    print(a)
else:
    print("Input sbagliato, inserire stringa maggiore di 2 caratteri")
