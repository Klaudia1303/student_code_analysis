def Ex8(file):
    pattern=r'[A-Z]{3}[ ]*[A-Z]{3}[ ]*([0-9]{2})[ ]*([A-Z])[ ]*([0-9]{2})[ ]*[A-Z][ ]*[0-9]{3}[ ]*[A-Z][ ]*'
    mesi={'A':['01',31],'B':['02',28],'C':['03',31],'D':['04',30],\
          'E':['05',31],'H':['06',30],'L':['07',31],'A':['08',31],\
          'P':['09',30],'R':['10',31],'S':['11',30],'T':['12',31]}; lista=[]
    with open(file,encoding="UTF-8") as fin:
        Data=[line.strip() for line in fin.readlines()]
    for line in Data:
        if re.search(pattern,line):
            data=''
            if re.search(pattern,line).group(2) in mesi:
                for key in mesi:
                    if key==re.search(pattern,line).group(2):
                        giorno=int(re.search(pattern,line).group(3))
                        if giorno>40: giorno-=40
                        if 0<giorno<=mesi[key][1]:
                            if giorno<10: data+='0'+str(giorno)+'/'+mesi[key][0]+'/'
                            else: data+=str(giorno)+'/'+mesi[key][0]+'/'
                            if int(re.search(pattern,line).group(1))>20:
                                data+=str(1900+int(re.search(pattern,line).group(1)))
                            else: data+=str(2000+int(re.search(pattern,line).group(1)))
                            lista.append(data); break
                        else:   lista.append('Giorno errato')
            else:   lista.append('Mese errato')
        else:   lista.append('Codice errato')
    return lista
    """with open(file,encoding="UTF-8") as fin:
        Data=[line.strip() for line in fin.readlines()]
    #pattern=r'^(([A-Z]{3})\s?){2}(\d{2}([DHPS]([37]0|[1245]\d|0\d)|[ACELMRT]([37][01]|[12456]\d|0\d)|B(6[0-8]|[45]\d|2[0-8]|1\d|0\d)))\s?([A-Z]\d{3}[A-Z])$'
    lista=[]
    for line in Data:
        contr=True
        #if re.search(pattern,fin): print(re.search(pattern,fin).group()); lista.append()
        if len(line)==16 and (line[:6].isupper() and line[:6].isalpha()) and -1<int(line[6:8])<99 and line[8] in ['A','B','C','D','E','H','L','M','P','R','S','T'] and line[9:11].isdecimal() and (line[11].isupper() and line[11].isalpha()) and line[12:15].isdecimal() and (line[15].isupper() and line[15].isalpha()):
            data=""; l1=['A','C','E','L','M','R','T']; l2=['D','H','P','S']; t=(('01','A'),('02','B'),('03','C'),('04','D'),('05','E'),('06','H'),('07','L'),('08','M'),('09','P'),('10','R'),('11','S'),('12','T'))
            if line[8] in l1 and 0<int(line[9:11])-40<32: data+=str(int(line[9:11])-40)+"/"
            elif line[8] in l1 and not(0<int(line[9:11])-40<32): data+=line[9:11]+"/"
            elif line[8]=='B' and 0<int(line[9:11])-40<29: data+=str(int(line[9:11])-40)+"/"
            elif line[8] in l1 and not(0<int(line[9:11])-40<29): data+=line[9:11]+"/"
            elif line[8] in l2 and 0<int(line[9:11])-40<31:   data+=str(int(line[9:11])-40)+"/"
            elif line[8] in l2 and not(0<int(line[9:11])-40<31):   data+=line[9:11]+"/"
            else: lista.append('Mese errato'); contr=False
            if contr:
                for elem in t:
                    if elem[1]==line[8]: data+=elem[0]+"/"
                if int(line[6:8])>=20: anno='19'+line[6:8]
                else: anno='20'+line[6:8]
                data+=anno
                lista.append(data)
        else: lista.append("Codice errato")
    return lista"""
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
