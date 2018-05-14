# -*- encoding=utf-8 -*-
# 计数排序
def count_sort(a):
    while "" in a:                              # 删除没有输入造成的空元素
        a.remove("")
    n = len(a)
    b = [None]*n                                # 造个新容器
    for i in range(n):
        p = 0
        q = 0
        for j in range(n):
            if int(a[j]) < int(a[i]):           # 对该值之前的数的个数进行分类累加
                p += 1
            elif int(a[j]) == int(a[i]):
                q += 1
        for k in range(p,p+q):
            b[k] = a[i]
    print("共收到{}个数".format(n))              # 输出结果，用逗号隔开
    print("排序结果为:",end = "")
    for l in range(n-1):
        print(b[l],end = ",")
    print(b[n-1])

if __name__ == '__main__':
    a = []
    b = int(input("想排序的个数："))             # 定制个数，依次输入
    for q in range(b):
        a.append(input("输入第{}个数:".format(q+1)))
    count_sort(a)