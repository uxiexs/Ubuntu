#!/usr/bin/python3
# coding:utf-8
# Example of calculating with dictionaries

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Find min and max price
# 为了对字典内容做运算，利用zip()将字典的键值反转。
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min price:', min_price)
print('max price:', max_price)

print('sorted prices:')
# 对数据排序只要使用zip()再配合sorted()就可以了。
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)
    # =======================================================================================================
    # 注意：zip()将创建一个迭代器，它的内容只能被消费一次：
    # prices_and_names = zip(price.values(), price.keys())
    # print（min(prices_and_names)) # OK
    # print(mzx(prices_and_names)) # ValueError: max() is an empty sequence
    # =======================================================================================================
