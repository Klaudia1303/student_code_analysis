s= " 'a32ppp7666"

i = 0
lunghezza = len(s)
max = 0

while (i < lunghezza): 
  count = s.count(s[i]) 
  if (count >= max):
    max = count 
    char = s[i]
  i += 1
print(char,max)
