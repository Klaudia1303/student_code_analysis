def A_Ex8(file):
    fi=open(file,'r',encoding="UTF-8")
    u=fi.readlines()
    d={}
    for riga in u:
        x=riga.strip().split(',')
        y=x[2]
        a=x[0]
        b=x[1]
        l1=[]
        l2=[]
        k=d.keys()
        if (y=='amici') and (a not in k) and (b not in k):
            l1.append(a)
            l2.append(b)
            d[a]=l2
            d[b]=l1
        elif (y=='amici') and (a in k) and (b not in k):
            q=list(d[a])
            l1.append(a)
            l2.append(b)
            c=[]
            c=q+l2
            c.sort()
            while c.count(b)>1:
                c.remove(b)
            d[a]=c
            d[b]=l1
        elif (y=='amici') and (a not in k) and (b in k):
            q=list(d[b])
            l1.append(a)
            l2.append(b)
            c=[]
            c=q+l1
            c.sort()
            while c.count(a)>1:
                c.remove(a)
            d[b]=c
            d[a]=l2
        elif (y=='amici') and (a in k) and (b in k):
            q=list(d[a])
            w=list(d[b])
            l1.append(a)
            l2.append(b)
            h=[]
            i=[]
            h=q+l2
            h.sort()
            while h.count(b)>1:
                h.remove(b)
            d[a]=h
            i=w+l1
            i.sort()
            while i.count(a)>1:
                i.remove(a)
            d[b]=i
        elif (y=='nemici') and (a in k) and (b not in k):
            r=d[a]
            if b in r:
                r.remove(b)
            d[a]=r
        elif (y=='nemici') and (a not in k) and (b in k):
            r=d[b]
            if a in r:
                r.remove(a)
            d[b]=r
        elif (y=='nemici') and (a in k) and (b in k):
            q=d[a]
            w=d[b]
            if b in q:
                q.remove(b)
            if a in w:
                w.remove(a)
            d[a]=q
            d[b]=w
    fi.close()
    return d




    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["amici1.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici2.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria'], 'Maria': ['Anna'], 'Paola': [], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici3.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici4.csv"] , {'Marco': ['Giorgio', 'Paolo'], 'Giorgio': ['Marco'], 'Paolo': ['Marco'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna']})
    counter_test_positivi += tester_fun(A_Ex8, ["amici5.csv"] , {'Marco': [], 'Giorgio': [], 'Paola': [], 'Anna': []})

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
