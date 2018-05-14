# -*- encoding=utf-8 -*-
# 鸡尾酒排序
def cockrail_sort(l):
    size = len(l)
    for i in range(size//2):                    # 两端遍历，只用循环一半
        for j in range(i,size-1-i):
            if l[j] > l[j+1]:                   # 冒出最大值
                l[j],l[j+1] = l[j+1],l[j]
        for k in range(size-2-i,i,-1):          # 冒出最小值
            if l[k] < l[k-1]:
                l[k],l[k-1] = l[k-1],l[k]
    print(l)

if __name__ == '__main__':
    l = list(input("输入列表"))
    cockrail_sort(l)