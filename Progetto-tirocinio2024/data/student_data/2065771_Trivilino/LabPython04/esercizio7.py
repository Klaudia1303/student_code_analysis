s=input('Inserire una stringa: ')
i=0
lett=''
volte=0
while i<len(s):
    if s.count(s[i])>volte:
        lett=s[i]
        volte=s.count(s[i])
    elif s.count(s[i])==volte:
        if s.rfind(lett)<s.rfind(s[i]):
            lett=s[i]
    i+=1
print(lett,'appare',volte,'volte')
        
