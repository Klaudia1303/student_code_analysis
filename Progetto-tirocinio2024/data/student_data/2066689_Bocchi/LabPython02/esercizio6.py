n = int(input('numeratore: '))
d = int(input('denominatore: '))

prop = n<d
app = n%d == 0

if prop:
    print('propria')
elif app:
    print('apparente')
elif n>d and n%d !=0:
    print('impropria')
