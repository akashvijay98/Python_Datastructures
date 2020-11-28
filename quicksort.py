def quicksort(a,low,high):
    
    if low <high:
        p=partition(a,low,high)
        quicksort(a,low,p-1)
        quicksort(a,p+1,high)
    
    return a
    
    
def partition(a,low,high):
    
    pivot=a[high]
    i=low-1
    
    for j in range(low,high):
        if a[j]<pivot:
            i+=1
            a[j],a[i]=a[i],a[j]
        
    a[i+1],a[high]=a[high],a[i+1]
    
    return i+1
    
    
a=[1,6,4,3,2]
print(quicksort(a,0,len(a)-1))   
