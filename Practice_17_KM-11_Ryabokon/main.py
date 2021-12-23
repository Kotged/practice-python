from factorial import factorial
from exp_root import exponentation, root
from logarithm import logarithm
def main():
    while 1>0:
        print('-'*20)
        print('If you want to find the factorial of the number enter 0 \nIf you want to find the square of the number enter 1 \nIf you want to find a cube of the number enter 2 \nIf you want to find the square root of the number enter 3 \nIf you want to find the cubic root of the number enter 4 \nIf you want to find the logarithm of the number enter 5 \nIf you want to find the natural logarithm of the number enter 6 \nIf you want to find the decimal logatithm of the number enter 7  ')
        print('-'*20)
        ans = input('Select an option: ')
        if ans == '0':
            while 1>0:
                n=float(input('Enter a natural number: '))
                if n<0 or n%1!=0:
                    print('Error. The number must be a natural.')
                else:
                    break
            print('The factorial of ', n, ' is ', factorial.fact(n))
        elif ans == '1':
            n=float(input('Enter a number: '))
            print('The square of ', n, ' is ', round(exponentation.exp2(n),3))
        elif ans == '2':
            n=float(input('Enter a number: '))
            print('The cube of ', n, ' is ', round(exponentation.exp3(n),3))
        elif ans == '3':
            while 1>0:
                n=float(input('Enter a positive number: '))
                if n<0:
                    print('Error. The number must be positive.')
                else:
                    break
            print('The square root of ', n, ' is ', round(root.root2(n),3))
        elif ans == '4':
            n=float(input('Enter a number: '))
            if n<0:
                print('The cubic root of ', n, ' is ', root.root3(n))
            else:
                print('The cubic root of ', n, ' is ', round(root.root3(n),3))
        elif ans == '5':
            while 1>0:
                a=float(input('Enter a base of the logarithm: '))
                b=float(input('Enter a number: '))
                if a<=0 or a==1:
                    print('Error. The base of the logarithm must be positive and different from 1.')
                elif b<=0:
                    print('Error. The number must be positive.')
                else:
                    break
            print('The logarithm of ', b, ' with base ', a, ' is ', round(logarithm.log(a, b),3))
        elif ans == '6':
            while 1>0:
                b=float(input('Enter a number: '))
                if b<=0:
                    print('Error. The number must be positive.')
                else:
                    break
            print('The natural logarithm of ', b, ' is ', round(logarithm.ln(b),3))
        elif ans == '7':
            while 1>0:
                b=float(input('Enter a number: '))
                if b<=0:
                    print('Error. The number must be positive.')
                else:
                    break
            print('The demical logarithm of ', b, ' is ', round(logarithm.lg(b),3))
        else:
            print('This is a wrong input. Try again.')
        print('-'*20)
        again=input('Do you want to test again? (yes/no) ').lower()
        if again == 'yes':
            continue
        elif again == 'no':
            break
        else:
            print('This is a wrong input. Try again.')
        print('-'*20)
if __name__ == '__main__':
    main()