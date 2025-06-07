def ins(val):
    b=True
    while b:
        print("Inserire la",val,"stringa: ",end=""); k=input()
        if k!="": b=False
        else: print("\n\tStringa vuota. Si prega di reinserire\n")
    return k
def massimo(uno,due):
    c=len(uno); b=len(due)
    if max(c,b)==c: m=uno
    else: m=due
    return m
s1=ins("prima"); s2=ins("seconda"); s=a=""; b=False
for i in range(len(s1)):
    if b:   a=""
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            if i+1<len(s1) and j+1<len(s2) and s1[i+1]==s2[j+1]:
                a+=s1[i]; b=False
            elif ((i-1)>0 and (j-1)>0) and s1[i-1]==s2[j-1]:
                a+=s1[i]; s=massimo(s,a); b=True; break
print("Sequenza di caratteri più lunga di s1 in s2:",s)
