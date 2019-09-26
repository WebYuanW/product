import os

def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價錢' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
    return products

def user_input(products):
    while True:
        name = input('請輸入商品名稱： ')
        if name == 'q':
            break
        price = input('請輸入商品價格： ')
        products.append([name, price])
    print(products)
    return products

def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

def write_file(filename, products):
    with open(filename, 'w', encoding= 'utf-8') as f:
        f.write('商品,價錢\n')
        for d in products:
            f.write(d[0] + ',' + d[1] + '\n')

def main():
    if os.path.isfile('product.csv'):
        print('找到檔案')
        products = read_file('product.csv')
    else:
        print('找不到檔案')
    
    products = user_input(products)
    print_products(products)
    write_file('product.csv', products)

main()