s1=input('inserire stringa 1: ')
s2=input('inserire stringa 2: ')
somma=' '
for i in range(0,len(s1)):
            if s1[i] not in s2:
                somma += s1[i]
print(somma)
