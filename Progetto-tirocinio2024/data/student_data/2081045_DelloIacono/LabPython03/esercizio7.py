c=input('inserire un carattere: ')
print('inserire una stringa: ')
app=0
while (app<=2):
    s=str(input())
    app=s.count(c)
print(app)
