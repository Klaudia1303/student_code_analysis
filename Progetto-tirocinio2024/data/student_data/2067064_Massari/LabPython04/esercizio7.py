s=input('inserisci una stringa: ')
n=0
var1=0
var2=''
while n<len(s):
      var3=s.count(s[n])
      var4=s[n]
      if var3>=var1:
            var1=var3
            var2=var4
      n=n+1
print(var2)
      


