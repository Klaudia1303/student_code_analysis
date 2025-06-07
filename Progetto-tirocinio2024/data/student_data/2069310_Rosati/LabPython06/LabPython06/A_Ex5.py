mas=0
let=''
s=input("Inserisci una stringa alfanumerica: ")
for i in range(len(s)):
    bol=True
    c=0
    for j in range(i,len(s)):
        if bol==True:
           if s[i]==s[j]:
              c+=1
           else:
              bol=False
    if c>=mas:
       mas=c
       let=s[i]
print(let,mas)
