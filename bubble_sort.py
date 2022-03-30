# 冒泡排序

import random


def bubble_sort(li):
    length = len(li)
    for i in range(length - 1): # 需要比较的次数(因为最后一个已经是最小的，不需要再进行比较)
        exchange = False
        for j in range(length - i - 1): # 指针运行的位置，需要减去已经排序好的和最后一次不需要排序的
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            continue

list = [random.randint(0, 1000) for i in range(100)]
bubble_sort(list)
print(list)