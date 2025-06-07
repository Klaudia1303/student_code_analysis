n=input("Inserisci un numero(*per terminare): ")
c=0
while n!= "*":
      if n< "0":
          c=c+int(n)
      n=input(" Inserisci un numero(* per terminare): ")
print(c)
