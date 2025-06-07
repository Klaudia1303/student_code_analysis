s1=input('Inserire stringa:')
s2=input("Inserire un'altra stringa:")
for carattere in (range(len(s1))):
            if s1[carattere] not in s2:
                print(s1[carattere])
