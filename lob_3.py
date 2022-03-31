#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import random
import time


def running_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f"Running time is {t2 - t1}")
    return wrapper


@running_time
def bubble_sort(list):
    length = len(list)
    for i in range(length - 1):
        exchange = False
        for j in range(length - 1 - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                exchange = True
        if not exchange:
            return


@running_time
def select_sort(list):
    length = len(list)
    for i in range(length - 1):
        min_doc = i
        for j in range(i+1, length):
            if list[j] < list[min_doc]:
                min_doc = j
        list[i], list[min_doc] = list[min_doc], list[i]


@running_time
def insert_sort(list):
    length = len(list)
    for i in range(1, length):
        tmp = list[i]
        j = i - 1
        while j >=0 and list[j] > tmp:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = tmp


if __name__ == '__main__':
    l1 = list(range(10000))
    random.shuffle(l1)
    bubble_sort(l1)