s=input("Inserisci una stringa: ")
l=0 
i=0
while i!=len(s):
      c=s.count(s[i])
      if c>=l:
         let=s[i]
         l=c         
      i=i+1
print(let)
