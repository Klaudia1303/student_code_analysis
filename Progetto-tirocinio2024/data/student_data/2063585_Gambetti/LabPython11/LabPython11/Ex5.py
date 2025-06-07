def Ex5(file):
    f=open(file,encoding='UTF-8')
    d={}
    d['auto']=0
    d['moto']=0
    d['ciclomotore1']=0
    d['ciclomotore2']=0
    d['errata']=0
    riga=f.readlines()
    for r in riga:
        r=r.strip().split('\n')
        j=0
        l=0
        if int(len(r[0]))<5 or int(len(r[0])>7):
            d["errata"]+=1
        if(len(r[0])==7):
            if r[0][0].isupper() and r[0][1].isupper() and r[0][2].isdigit() and r[0][3].isdigit() and r[0][4].isdigit():
                if r[0][5].isdigit() and r[0][6].isdigit():
                    d["moto"]+=1
                if not r[0][5].isdigit() and r[0][6].isdigit():
                    d["errata"]+=1
                if r[0][5].isupper() and r[0][6].isupper():
                    d["auto"]+=1
                if not r[0][5].isupper() and r[0][6].isupper():
                    d["errata"]+=1
            else:
                 d["errata"]+=1
        if(len(r[0])==5):
            for i in range(5):
                if(r[0][i].isupper() or r[0][i].isdigit()):
                    j+=1
            if j==5:
                d["ciclomotore1"]+=1
            else:
                d["errata"]+=1
        if(len(r[0])==6):
            for i in range(6):
                if(r[0][i].isupper() or r[0][i].isdigit()):
                    l+=1
            print(l)
            if l==6:
                d["ciclomotore2"]+=1
            else:
                d["errata"]+=1
    return d
      
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, ["targhe1.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 1})
    counter_test_positivi += tester_fun(Ex5, ["targhe2.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 2})
    counter_test_positivi += tester_fun(Ex5, ["targhe3.txt"] , {'auto': 3, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 3})
    counter_test_positivi += tester_fun(Ex5, ["targhe4.txt"] , {'auto': 3, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 4})
    counter_test_positivi += tester_fun(Ex5, ["targhe5.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 5})
    
    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
