num=int(input('inserire numeratore: '))
den=int(input('inserire denominatore: '))
if (num<den):
        print('propria')
if (num%den==0):
        print('apparente')
if (num>den and not num%den==0):
        print('impropria')
