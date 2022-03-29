# 冒泡排序

import random


def bubble_sort(li):
    length = len(li)
    for i in range(length - 1): # 需要排序的数
        exchange = False
        for j in range(length - i - 1): # 每次对比的数
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            continue

list = [random.randint(0, 1000) for i in range(100)]
bubble_sort(list)
print(list)