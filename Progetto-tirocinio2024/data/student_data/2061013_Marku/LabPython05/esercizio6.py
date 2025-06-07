s=input('inserire una stringa: ')
mas=0
for c in range(len(s)):
   if s.rfind(s[c])-s.find(s[c])>mas:
      mas=s.rfind(s[c])-s.find(s[c])
print(mas)
  
