phrase1=input('Enter the phrase: ').lower()
x=set()
for el in phrase1:
    if el.isalpha():
        x.add(el)
phrase2=input('Enter another phrase: ').lower()
y=set()
for el in phrase2:
    if el.isalpha():
        y.add(el)
if x&y==y:
    print('Set of letters of the first phrase: ',x,'\n Set of letters of the second phrase: ',y, '\n The second phrase can be composed of the letters of first.')
else:
    print('Set of letters of the first phrase: ',x,'\n Set of letters of the second phrase: ',y, '\n The second phrase cannot be composed of the letters of first.')