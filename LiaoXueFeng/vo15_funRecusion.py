#/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# 汉诺塔问题有三根柱子，我给它们分别命名为起始柱src，临时柱tmp，目的柱dst
# 盘子一共分两种情况：
# 1.只有1个盘子 : 这种情况下，直接从起始柱src 移动到 目的柱dst ,完成任务。
# 2.有1个以上的盘子 :
# 假如有n个盘子在起始柱，
# step1:首先把第n个盘子上方的n-1个盘子搬到临时柱。
# step2:然后把第n个盘子从起始柱移动到目的柱
# step3:最后把n-1个盘子从临时柱搬到目的柱 任务完成
#*******************************************************************************
def move(fro,to): #把盘子从fro移到to
    print(fro,'->',to)

def hanoi(n,src,tmp,dst):
    if n == 1: # 只有一个盘子的情况下
        move(src,dst)
    else: # 一个以上盘子的情况
        hanoi(n-1,src,dst,tmp) # 将盘子从src移动到tmp
        move(src,dst) # 将第n个盘子从src移到dst
        hanoi(n-1,tmp,src,dst) # 将tmp上的盘子移动到dst
n = input("Plese input the number:")
hanoi(int(n),'A','B','C')
