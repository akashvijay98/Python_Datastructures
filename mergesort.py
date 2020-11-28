def mergesort(a):
    if len(a) > 1:
        m = len(a)//2
        
    
        L=a[:m]
        R=a[m:]
        
       
        
        mergesort(L)
        
        mergesort(R)
        
        i = j = k = 0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                a[k] = L[i]

                i += 1
                
            else:
                a[k]=R[j]
                j += 1
            k += 1
            
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1 

                

        
a=[1,5,4,3,6]

print("before sort",a)        
mergesort(a)
print("after sort",a)
