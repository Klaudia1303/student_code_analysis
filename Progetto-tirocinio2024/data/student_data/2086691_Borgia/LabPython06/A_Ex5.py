s=input('Inserire una stringa alfanumerica: ')
mass=1
v=''
for i in range(1,len(s)):
   if s[i]!=v:
      mass=1
   if s[i-1]==s[i]:
      mass=mass+1
      v=s[i]
print(v,mass)
