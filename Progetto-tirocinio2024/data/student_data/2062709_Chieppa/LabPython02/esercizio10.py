cane=float(input('inserire età cane: '))
if 0.001<=cane<=2.0 and cane>0:
    print('età umana:',cane*10.5)
elif 2.0<cane:
    print('età umana:',21+((cane-2.0)*4))
