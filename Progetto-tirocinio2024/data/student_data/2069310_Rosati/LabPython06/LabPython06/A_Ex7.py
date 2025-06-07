s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
mas=""
cont=0
for i in range(len(s1)):
    for j in range(len(s1)):
          let=s1[i:j+1]
          if let in s2 and len(let)>cont:
             cont=len(let)
             mas=let
          
print(mas)
