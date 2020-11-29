a=[9,2,3,5,6,4,3,8,6,9,5]

def selection(a):
    for i in range(len(a)):
        m=i
        for j in range(i+1,len(a)):
            if a[m]>a[j]:
                m=j
        a[m],a[i]=a[i],a[m]
    return a
                
selection(a)

 
