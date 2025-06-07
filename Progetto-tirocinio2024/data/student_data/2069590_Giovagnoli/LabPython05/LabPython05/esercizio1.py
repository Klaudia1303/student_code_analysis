s=input("Inserire una stringa: ")
s1= input("Inserire una stringa con lo stesso numero di caratteri della prima: ")
if len(s)==len(s1):
    s_finale=""
    for i in range(len(s)):
        s_finale=s_finale+s[i]+s1[i]
    print(s_finale)