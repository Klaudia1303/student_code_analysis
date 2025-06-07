s=str(input('inserire stringa 1: '))
t=str(input('inserire stringa 2: '))
carattere_s=s[-1]
carattere_t=t[0]
check= True
while check and carattere_s!=carattere_t:
    s=str(input('inserire stringa 1: '))
    t=str(input('inserire stringa 2: '))
    carattere_s=s[-1]
    carattere_t=t[0]
    if carattere_s==carattere_t:
        check= False
print(s,t)
