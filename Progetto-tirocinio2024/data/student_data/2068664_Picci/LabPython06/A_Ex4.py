v1=20
v2=1
s2=0
for i in range(1,1000):
    s1=i*v1
    s2+=i
    if s2>=s1:
        break
print("Il viaggiatore 2 impiega",i,"giorni")
