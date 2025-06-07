s1=input('Inserire prima stringa:')
s2=input('Inserire seconda stringa')
if len(s1)==len(s2):
  for i in range(len(s1)) and range(len(s2)):
    print(s1[i]+s2[i])
