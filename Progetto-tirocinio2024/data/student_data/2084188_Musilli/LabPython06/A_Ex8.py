def ins(val):
    b=True
    while b:
        print("Inserire la",val,"stringa: ",end=""); k=input()
        if k!="": b=False
        else: print("\n\tStringa vuota. Si prega di reinserire\n")
    return k
s1=ins("prima"); s2=ins("seconda"); s=""
n=int(input("Inserire la distanza massima concessa: "))
for i in range(len(s1)):
    a=i-n; b=i+n
    if a<0: a=0; 
    if b>len(s2): b=len(s2)-1
    for j in range(a,b):
        if j<len(s2) and s1[i]==s2[j]: s+=s1[i]; break
print("\n\t\tStringa composta:\nCaratteri di s1 presenti anche in s2\n\
con posizione distante al massimo n da quella che hanno in s1:",s)
