# 冒泡排序
def bubble_sort(l):
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



# 插入排序
def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists



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





# 桶排序
def barrel_sort(qt):
    b = ([0],[1],[2],[3],[4],[5],[6],[7],[8],[9])       # 创建桶
    for i in qt:                                        # 把元素加到桶内
        for j in range(len(b)):
            if i <= str(b[j][0]):
                b[j].append(i)
                break
    for k in range(len(b)):                             # 确保空桶不会报错
        if len(b[k]) == 1:
            b[k].append('')       
    # print(b)
    # print("{}{}{}{}{}{}{}{}{}{}".format(b[0][0],b[1][0],b[2][0],b[3][0],b[4][0],b[5][0],b[6][0],b[7][0],b[8][0],b[9][0]))
    for l in range(len(b)):                             # 桶内会有多个元素
        print(b[l][1]*(len(b[l])-1),end = "")
    print("\t")

if __name__ == '__main__':
    qt = input("输入一串9以内的数：")
    barrel_sort(qt)


# 直接选择排序
def select_sort(lists):
    # 选择排序
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists





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





# 归并排序
def MergeSort(lists):                       # 函数作用为分开左右两边各一半
    if len(lists) <= 1:
        return lists
    num = int( len(lists)/2 )
    left = MergeSort(lists[:num])           # 递归迭代
    right = MergeSort(lists[num:])
    # 分解至单个元素
    return Merge(left, right)               # 左右两个参数是迭代动态变化的
def Merge(left,right):                      # 归并操作，每次都比较两个有序数组的第一个元素，直到某一边被用完
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result+= left[l:]
    return result
print(MergeSort([1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]))
# 前者作用是返回数组的两边
# 后者作用是归并两边并返回


# 堆排序
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)




# 基数排序
import math
def radix_sort(a, radix=10):
    """a为整数列表， radix为基数"""
    K = int(math.ceil(math.log(max(a), radix))) # 用K位数可表示任意整数
    bucket = [[] for i in range(radix)] # 不能用 [[]]*radix
    for i in range(1, K+1): # K次循环
        for val in a:
            bucket[val%(radix**i)/(radix**(i-1))].append(val) # 析取整数第K位数字 （从低到高）
        del a[:]
        for each in bucket:
            a.extend(each) # 桶合并
        bucket = [[] for i in range(radix)]




# 希尔排序
def shell_sort(arr):
    n=len(arr)
    h=1
    while h<n/3:
        h=3*h+1
    while h>=1:
        for i in range(h,n):
            j=i
            while j>=h and arr[j]<arr[j-h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j-=h
        h=h/3
    print(arr)




#quick sort
def quick_sort(L, low, high):
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1                                                             
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1 
        L[j] = L[i]
    L[i] = key 
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L