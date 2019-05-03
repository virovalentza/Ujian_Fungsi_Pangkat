
x = input('Masukan nilai x:')
y = input ('Masukan nilai y:')

def xpangkaty(x,y):
    if int(y)== 0:
       return 1
    else:
        return int(x)*xpangkaty(x,int(y)-1)

print ('x pangkat y=', xpangkaty(x,y))

