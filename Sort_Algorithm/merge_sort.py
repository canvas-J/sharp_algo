# -*- encoding=utf-8 -*-
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