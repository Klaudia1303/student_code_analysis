base=int(input('insert number: '))
base0=1
spaces=int((base-1)/2)
for counter in range(0,base):
    print(' '*spaces+'*'*base0)
    base0+=2
    spaces-=1
    if base0>base:
        break
