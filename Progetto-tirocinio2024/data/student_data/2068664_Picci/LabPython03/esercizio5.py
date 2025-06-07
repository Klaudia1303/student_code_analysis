s = "Casa"
while(s.isalpha() == False or s.islower() == False):
    s=input("inserisci una stringa:")
    if(s!=""):
        print(s[0] + s[len(s) - 1])
