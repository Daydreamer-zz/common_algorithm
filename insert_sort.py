# 插入排序
# 类比抓牌场景

def insert_sort(li):
    length = len(li)
    for i in range(1, length): # i表示摸到的牌的下标，从1开始(因为初始手里就有第一张牌)
        tmp = li[i]  # 摸到的牌的值
        j = i - 1 # j指的是现在手里最大值牌的下标
        while j >= 0 and li[j] > tmp: # 手里的牌比摸到的牌的值大
            li[j+1] = li[j] # 往右移
            j -= 1
        li[j+1] = tmp # 把摸到的牌插到合适位置


if __name__ == '__main__':
    li = [3, 2, 4, 1, 5, 7, 9, 6, 8]
    print(li)
    insert_sort(li)
    print(li)
