finito=False
while not finito:
    p=input('inserire stringa palindroma')
    if p==p[::-1]:
        finito=True
    else:
        print('non palindroma, inserire stringa palindroma')
print('stringa palindroma di lunghezza:', len(p))

