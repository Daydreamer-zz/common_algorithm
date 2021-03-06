# 选择排序

def select_sort(li):
    length = len(li)
    for i in range(length - 1):
        min_loc = i  # 最小数的下标，初始假设一开始的
        for j in range(i+1, length): # 遍历无序区数字，取出最小值下标赋值给min_loc
            if li[j] < li[min_loc]: # 依次和原最小值比较，
                min_loc = j  # 记录无序区最小数的位置
        li[i], li[min_loc] = li[min_loc], li[i] # 交换被比较的数和最小值的位置，即把最小值放第一个


li = [3, 4, 2, 1, 5, 8, 6, 7, 9]
print(li)
select_sort(li)
print(li)