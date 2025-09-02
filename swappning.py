def swap(n): #swapping list vals
    l=0
    r=len(n)-1
    while l<r:
        n[l],n[r]=n[r],n[l]
        l+=1
        r-=1
        
