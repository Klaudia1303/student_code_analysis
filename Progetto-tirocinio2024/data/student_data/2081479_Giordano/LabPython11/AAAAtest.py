def Ex5(file):
    import re
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    targhe={'auto': 0, 'moto': 0, 'ciclomotore1': 0, 'ciclomotore2': 0, 'errata': 0}     
    with open(file, encoding='UTF-8') as file:

        txt=file.readline()
        txt=txt.strip()
        while txt!='':
            if re.match(r'[A-Z][A-Z]\d\d\d[A-Z][A-Z]',txt):
                print(txt)
                targhe['auto']+=1
            elif re.match(r'[A-Z][A-Z]\d\d\d\d\d',txt):
                targhe['moto']+=1
            elif re.match(r'[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]',txt) and len(txt)==6:
                targhe['ciclomotore2']+=1
            elif re.match(r'[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]',txt) and len(txt)==5:
                targhe['ciclomotore1']+=1
            else:
                targhe['errata']+=1
            txt=file.readline()
            txt=txt.strip()
    print(targhe)
    return targhe

Ex5('targhe5.txt')
