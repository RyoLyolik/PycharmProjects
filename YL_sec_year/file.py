data = open('prices.txt', mode='r').read()
all = 0
if data != '':
    data = data.split('\n')
    for product in data:
        product = product.split()
        all += float(product[1]) * float(product[-1])

    if len(str(all).split('.')[-1]) < 2:
        all = str(all) + '0'

    elif len(str(all).split('.')) == 1:
        all = str(all) + '.00'


    print(all)

else:
    print('0.00')
