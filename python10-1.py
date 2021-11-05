print('Discount table:')
products_list = [29.25, 48.99, 99.98, 124.65, 214.30, 543.90, 799.85]
sell_list=list(map(lambda x: round(x*0.6, 2), products_list))
new_price=list(map(lambda x: round(x*0.4, 2), products_list))
for i in range(7):
    print(products_list[i], ' ',new_price[i],' ', sell_list[i])