s1 = ''
while len(s1) == 0:
    s1 = input("inserisci s1: ")

s2 = ''
while len(s2) == 0:
    s2 = input("inserisci s2: ")

subs = ''
for i in range(len(s1)):
    t_subs = ''
    t_i = i
    
    for j in range(len(s2)):        
        if s1[t_i] == s2[j]:
            t_subs += s2[j] 

            if t_i+1 >= len(s1):
                break   
            else:
                t_i += 1
    
    if len(t_subs) > len(subs):
        subs = t_subs

print(subs)
