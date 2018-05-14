# -*- encoding=utf-8 -*-
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
