s=input("Inserisci una stinga: ")
lungi=0
lungf=0
for i in range(len(s)):
    lungi=s.rfind(s[i])-i
    if lungi>=lungf:
       lungf=lungi
print(lungf)
