maggiore=False
s=input('Inserire una stringa: ')
s1=input('Inserire una stringa: ')
while not maggiore:
    s2=input('Inserire una stringa: ')
    if len(s)+len(s1)==len(s2):
        maggiore=True
        print(s,s1,s2)
    else:
        s=s1
        len(s)==len(s1)
        s1=s2
        len(s1)==len(s2)
