# -*- encoding=utf-8 -*-
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