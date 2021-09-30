print('Discount table:')
products_list = [29.25, 48.99, 99.98, 124.65, 214.30, 543.90, 799.85]
sell_list=[]
new_price_list=[]
for i in products_list:
    sell_list.append(round(i*0.6,2))
    new_price_list.append(round(i*0.4,2))
for i in range(0,7):
    print(products_list[i], ' ',new_price_list[i],' ', sell_list[i])