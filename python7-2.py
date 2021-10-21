
num={'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
try:
    while True:
        basic=list(input('Enter 6 characters for RGB in hexadecimal system: '))
        new=[]
        if len(basic)!=6:
            print('There can be only 6 characters. Try again.')
            continue
        else:
            
            for el in basic:
                if el.isdigit():
                    new.append(int(el)*16)
                elif el in num:
                   new.append(num[el]*16)       
                else:
                    pass
            
            a=int(new[0])+int(new[1])
            b=int(new[2])+int(new[3])
            c=int(new[4])+int(new[5])
                        
        print('Your color number in decimal system (', a,'',b,'',c,')')
        break
except:
    print('Wrong syntax')
