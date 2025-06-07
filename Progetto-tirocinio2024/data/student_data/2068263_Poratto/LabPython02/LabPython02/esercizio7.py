a1n=int(input('inserisci un numero: '))
a2n=int(input('inserisci un numero: '))
a3n=int(input('inserisci un numero: '))
if a1n<a2n<a3n:
    print(a3n,a2n,a1n)
elif a1n<a3n<a2n:
    print(a2n,a3n,a1n)
elif a2n<a1n<a3n:
    print(a3n,a1n,a2n)
elif a2n<a3n<a1n:
    print(a1n,a3n,a2n)
elif a3n<a1n<a2n:
    print(a2n<a1n<a3n)
elif a3n<a2n<a1n:
    print(a1n,a2n,a3n)
