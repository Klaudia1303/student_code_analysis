def Ex5(file):
    import re
    d={}
    d["auto"]=0
    d["moto"]=0
    d["ciclomotore1"]=0
    d["ciclomotore2"]=0
    d["errata"]=0
    fin=open(file,"r",encoding="UTF-8")
    riga=fin.readline()
    patternAuto=r'\b[A-Z][A-Z][0-9][0-9][0-9][A-Z][A-Z]\b'
    patternMoto=r'\b[A-Z][A-Z][0-9][0-9][0-9][0-9][0-9]\b'
    patternCiclomotore1=r'\b[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]\b'
    patternCiclomotore2=r'\b[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]\b'
    while len(riga)>1:
        riga=riga.strip().split()
        s=riga[0]
        if len(re.findall(patternAuto,s))>=1:
            d["auto"]+=1
        elif len(re.findall(patternMoto,s))>=1:
            d["moto"]+=1
        elif len(re.findall(patternCiclomotore1,s))>=1:
            d["ciclomotore1"]+=1
        elif len(re.findall(patternCiclomotore2,s))>=1:
            d["ciclomotore2"]+=1
        else:
            d["errata"]+=1
        riga=fin.readline()
    fin.close()
    return d

#"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
      
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
