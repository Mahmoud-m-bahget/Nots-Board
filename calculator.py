print ( ' welcome to mahmoud calculator')
y = float(input('enter the first number ? \n '))
operation=input( 'chose the operation that you want from this list [ + , - , * , / ] \t')
x = float(input('enter the seccond  number ? \n'))

z = 0
if operation == '+' :
    z = y + x
    print( y ,'+' , x , '=' ,  z)
elif operation == '*' :
    z = y * x
    print( y ,'*' , x , '=' ,  z)
elif operation == '-' :
    z = y - x
    print( y ,'-' , x , '=' ,  z)
elif operation == '/' :
    if x == 0 :
        print('we are sorry we can not divide a number by 0 ')
    else:
        z = y / x
        print(y, '/', x, '=', z)
else:
    print("i'm sorry but my calculator can't do more than [ + , - , * , / ] ")
