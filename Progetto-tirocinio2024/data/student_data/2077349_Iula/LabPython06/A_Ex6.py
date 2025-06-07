a="349776123345679876543234567876543234569055"
t=9510990939794952322311710154344301747012051743844839
for i in range(11,100):
    somma=0
    for p in range(len(a)):
        m=int(a[p])*(i**(len(a)-1-p))
        somma=m+somma
    if somma==t:
        print(i)
        break

