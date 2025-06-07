
print("Tabellina in base ottale:")

for a in range(1,9):
    for b in range(1,9):
        p=a*b
        s=''
        while p>=8:
            resto=p-((p//8)*8)
            s=s+str(resto)
            p=p//8

        s=s+str(p)
        print(s[::-1], end='\t')
    print()



