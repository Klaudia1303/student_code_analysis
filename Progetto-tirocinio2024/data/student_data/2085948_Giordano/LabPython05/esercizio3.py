s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
s1_new=''
for i in s1:
    if i not in s2:
        s1_new += i
s1 = s1_new
print(s1)



