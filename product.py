products = []
with open('product.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價錢' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    products.append([name, price])
print(products)

for p in products:
    print(p[0], '的價格是', p[1])

with open('product.csv', 'w', encoding= 'utf-8') as f:
    f.write('商品,價錢\n')
    for d in products:
        f.write(p[0] + ',' + p[1] + '\n')
