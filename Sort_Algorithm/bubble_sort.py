# -*- encoding=utf-8 -*-
# 冒泡排序
def bubble(l):
    lens = len(l)
    while lens > 0:                     # 遍历所有元素个遍数
        for j in range(lens-1):         # 一圈冒出一个最大值，前面冒过的不再遍历
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
        lens -= 1
    print(l)

if __name__ == '__main__':
    l = list(input("输入列表"))
    bubble(l)