
s1=input(("inserisci stringa 1: "))
s2=input(("inserisci stringa 2: "))
if len(s1)==len(s2):
    for i in range(len(s1)):
        print(s1[i],end="")
        print(s2[i],end="")
else:
    print("le due stringhe hanno diversa lungezza di caratteri")
