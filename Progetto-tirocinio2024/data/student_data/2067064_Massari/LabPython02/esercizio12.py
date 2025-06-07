temp = float(input('inserire la temperatura: '))
s = input('inserie F o C per indicare la scala: ')
conv = (temp-32)/1.8
if s=='F':
    if conv<=0:
        print('solida')
    elif conv>=100:
        print('gassosa')
    elif 1<conv<99:
        print('liquida')
if s=='C':
    if temp<=0:
        print('solida')
    elif temp>=100:
        print('gassosa')
    elif 1<temp<99:
        print('liquida')
