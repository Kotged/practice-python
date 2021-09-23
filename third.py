years=float(input('Enter the age of your dog: '))
if years>=0 and years<=2:
    age=years*10.5
    print('Your dog`s age in the "dog years" is equal to ' + str(age))
elif years>2:
    age=(years-2)*4+21
    print('Your dog`s age in the "dog years" is equal to ' + str(age))
elif years<0:
    print('Your dog`s age cannot be negative')

