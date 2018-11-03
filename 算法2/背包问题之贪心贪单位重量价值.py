def tanxin(w,v,c):
    x=[0 for i in range (len(w))]
    for i in range(len(w)):
        x[i]=float(v[i]/w[i])
    x.sort()
    print("按单位重量的价值排序为：",x)
    t=[0 for i in range (len(w))]
    for j in range(len(w)):
         for i in range(len(w)):
            if float(v[i]/w[i])==x[j]:
                t[j]=i
                break
    print("对引的在元排列中的索引为：",t)
    sumW=0
    sumV=0
    for index in range(len(w)-1,-1,-1):
        if sumW<c and w[t[index]]<c-sumW :
            sumV+=v[t[index]]
            sumW+=w[t[index]]
        else:
            print(index)
            break
    print("此时到了：",index)
    print("此时的总价值为：",sumV)
    print("此时的总重量为：",sumW)
    res=c-sumW
    print("剩余容量为：",res)
    sumV=sumV+res*float(v[t[index]]/w[t[index]] )
    print("最终结果为：",sumV)




if __name__== '__main__':
 w=[1,3,4,5,1.5]
 v=[3,5,6,12,7]
 tanxin(w,v,10)


