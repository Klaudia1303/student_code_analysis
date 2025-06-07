equal=False
string1=''
string2=''
string3=''
while not equal:
    string1=input('insert string ')
    if len(string1)==len(string2)+len(string3):
        equal=True
    else:
        string3=string2
        string2=string1
print(string3,string2,string1)