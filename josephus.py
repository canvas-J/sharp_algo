#/usr/bin/env python
# coding=utf-8

class Node():  
    def __init__(self,value,next=None):  
        self.value=value  
        self.next=next  
  
def createLink(n):  
    if n<=0:  
        return False  
    if n==1:  
        return Node(1)  
    else:  
        root=Node(1)  
        tmp=root  
        for i in range(2,n+1):  
            tmp.next=Node(i)  
            tmp=tmp.next  
        tmp.next=root  
        return root  
  
def showLink(root):  
    tmp=root  
    while True:  
        print(tmp.value)  
        tmp=tmp.next  
        if tmp==None or tmp==root:  
            break  
  
def josephus(n,k):  
    if k==1:  
        print('survive:',n)  
        return  
    root=createLink(n)  
    tmp=root  
    while True:  
        for i in range(k-2):  
            tmp=tmp.next  
        print('kill:',tmp.next.value)  
        tmp.next=tmp.next.next  
        tmp=tmp.next  
        if tmp.next==tmp:  
            break  
    print('survive:',tmp.value)  
  
if __name__=='__main__':  
    josephus(10,4)  
    print('-----------------')  
    josephus(10,2)  
    print('-----------------')  
    josephus(10,1)  
    print('-----------------')  



# 改进版
def josephus(n,k):  
    if k==1:  
        print('survive:',n)  
        return  
    p=0  
    people=list(range(1,n+1))  
    while True:  
        if len(people)==1:  
            break  
        p=(p+(k-1))%len(people)  
        print('kill:',people[p])  
        del people[p]  
    print('survive:',people[0])  
  
if __name__=='__main__':  
    josephus(10,4)  
    josephus(10,2)  
    josephus(10,1)  


