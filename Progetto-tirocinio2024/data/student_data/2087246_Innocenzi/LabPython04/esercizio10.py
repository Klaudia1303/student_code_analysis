s_1=''
s_2=''
s_3=''
c=True

while(True):
    if(c):
        s_1=input("Inserisci una stringa: ")
        s_2=input("Inserisci una stringa: ")
        s_3=input("Inserisci una stringa: ")
        c=False
    if(len(s_1)+len(s_2)==len(s_3)):
        print(s_1, s_2, s_3)
        break
    else:
        s_1=s_2
        s_2=s_3
        s_3= input("Inserisci una stringa: ")

