import math
try:
    a=float(input('Enter the coefficient a: '))
    b=float(input('Enter the coefficient b: '))
    c=float(input('Enter the coefficient c: '))
    d=b*b-4*a*c
    if d<0:
        raise Exception
    sqrt_d=math.sqrt(d)
    x1=(-b+sqrt_d)/(2*a)
    x2=(-b-sqrt_d)/(2*a)
    if x1==x2:
        print('The equation has only one root')
    else:
       print('The equation has two roots') 
except ValueError:
    print('Error of entered values. The coefficients must be numbers. Try again')
except ZeroDivisionError:
    print('Zero division error. Coefficient a can not equal to zero. Try again')
except Exception:
    print('The equation has no roots')