def tanxinW(w,v,c):
    x = [0 for i in range(len(v))]
    t=v
    print(sorted(v))
    print(v)
    print(t)
    for i  in range(len(v)):
        for j in range(len(t)):
            if sorted(v)[i]==t[j]:
               x[i]=j
               break
            else:
                pass
    print(x)
    sumW=0
    sumV=0
    for i in range(len(v)-1,-1,-1):
        if sumW<c and w[x[i]]<c-sumW:
            sumW=sumW+w[x[i]]
            sumV=sumV+v[x[i]]

        else:
            print(i)
            break
    print("目前的重量：", sumW)
    print("目前的价值：", sumV)
    res=c-sumW
    print("剩余的空间：", res)
    sumV=sumV+float(res/w[x[i]]*v[x[i]])
    print("最终价值为：",sumV)






if __name__== '__main__':
 w=[1,3,4,5,1.5]
 v=[3,5,6,12,7]
 tanxinW(w,v,10)


