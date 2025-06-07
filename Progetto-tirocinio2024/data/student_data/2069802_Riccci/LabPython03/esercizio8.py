s=input("inserisici stringa palindroma --> ")
s1=""
for i in range(1,len(s)+1):
        s1+=s[len(s)-i]
while(s!=s1):
    s = input("non palindroma, inserisici stringa palindroma --> ")
    for i in range(1,len(s)+1):
        s1+=s[len(s)-i]
print("Stringa palindroma di lunghezza ",len(s))
