def Ex8(file):
    import re
    ris=[]
    fin=open(file,"r",encoding="UTF-8")
    pattern=r'\b[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]\b'
    for riga in fin:
        riga=riga.strip().replace(" ","")
        #controllo codice:
        if len(re.findall(pattern,riga))!=1:
            ris.append("Codice errato")
            continue
        #controllo del mese:
        if riga[8] not in ("ABCDEHLMPRST"):
            ris.append("Mese errato")
            continue
        if len(re.findall(pattern,riga))==1 and riga[8]in("ABCDEHLMPRST"):
            #controllo del giorno:
            if riga[8]in("ACELMRT") and (int(riga[9]+riga[10])<1 or 31<int(riga[9]+riga[10])<41 or int(riga[9]+riga[10])>71):
                ris.append("Giorno errato")
                continue
            if riga[8]in("DHPS") and (int(riga[9]+riga[10])<1 or 30<int(riga[9]+riga[10])<41 or int(riga[9]+riga[10])>70):
                ris.append("Giorno errato")
                continue
            if riga[8]in("B") and (int(riga[9]+riga[10])<1 or 28<int(riga[9]+riga[10])<41 or int(riga[9]+riga[10])>68):
                ris.append("Giorno errato")
                continue
            #calcolo dell'anno:
            if int(riga[6]+riga[7])<=20:
                anno="20"+str(riga[6]+riga[7])
            else:
                anno="19"+str(riga[6]+riga[7])
            #calcolo del mese:
            if riga[8]=="A":
                mese="01"
            elif riga[8]=="B":
                mese="02"
            elif riga[8]=="C":
                mese="03"
            elif riga[8]=="D":
                mese="04"
            elif riga[8]=="E":
                mese="05"
            elif riga[8]=="H":
                mese="06"
            elif riga[8]=="L":
                mese="07"
            elif riga[8]=="M":
                mese="08"
            elif riga[8]=="P":
                mese="09"
            elif riga[8]=="R":
                mese="10"
            elif riga[8]=="S":
                mese="11"
            elif riga[8]=="T":
                mese="12"
            #calcolo del giorno:
            if mese=="01" or mese=="03" or mese=="05" or mese=="07" or mese=="08" or mese=="10" or mese=="12":
                if 1<=int(riga[9]+riga[10])<=31:
                    if 1<=int(riga[9]+riga[10])<=9:
                        giorno="0"+str(int(riga[9]+riga[10]))
                    else:
                        giorno=str(int(riga[9]+riga[10]))
                elif 41<=int(riga[9]+riga[10])<=71:
                    if 1<=int(riga[9]+riga[10])-40<=9:
                        giorno="0"+str(int(riga[9]+riga[10])-40)
                    else:
                        giorno=str(int(riga[9]+riga[10])-40)
            if mese=="04" or mese=="06" or mese=="09" or mese=="11":
                if 1<=int(riga[9]+riga[10])<=30:
                    if 1<=int(riga[9]+riga[10])<=9:
                        giorno="0"+str(int(riga[9]+riga[10]))
                    else:
                        giorno=str(int(riga[9]+riga[10]))
                elif 41<=int(riga[9]+riga[10])<=70:
                    if 1<=int(riga[9]+riga[10])-40<=9:
                        giorno="0"+str(int(riga[9]+riga[10])-40)
                    else:
                        giorno=str(int(riga[9]+riga[10])-40)
            if mese=="02":
                if 1<=int(riga[9]+riga[10])<=28:
                    if 1<=int(riga[9]+riga[10])<=9:
                        giorno="0"+str(int(riga[9]+riga[10]))
                    else:
                        giorno=str(int(riga[9]+riga[10]))
                elif 41<=int(riga[9]+riga[10])<=68:
                    if 1<=int(riga[9]+riga[10])-40<=9:
                        giorno="0"+str(int(riga[9]+riga[10])-40)
                    else:
                        giorno=str(int(riga[9]+riga[10])-40)
            #risultato:
            ris.append(giorno+"/"+mese+"/"+anno)
    fin.close()
    return ris
#"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
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
