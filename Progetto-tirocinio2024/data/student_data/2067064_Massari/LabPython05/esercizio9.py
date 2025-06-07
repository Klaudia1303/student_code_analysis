s=int(input('inserire il lato del quadrato: '))
if s>=3 and s%2==1:
    for i in range(1,s+1):
        spazi=s-2

        if i==1:
            print('*'*s)
        if i>1 and i<s:
            print(str('*'+' '*spazi+'*'))
        if i==s:
            print('*'*s)
                  