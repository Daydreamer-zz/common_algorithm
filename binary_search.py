# 二分查找

from run_time import cal_time


@cal_time
def binary_search(list, value):
    left = 0
    right = len(list) - 1
    while left <= right: # 只要左边比右边小于或等于，说明目标还是可以继续查找的
        mid = (left + right) // 2  # 中间拆分
        if list[mid] == value:  # 中间的值正好等于目标值，直接返回
            return mid
        elif list[mid] > value:  # 中间值比目标值大，说明目标值在拆分后的左边
            right = mid - 1  # 把右边和的中间值丢弃
        else: # 中间值比目标值小的情况
            left = mid + 1
    return None


if __name__ == '__main__':
    l1 = list(range(100000000))
    binary_search(l1, 200000)