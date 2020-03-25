def perms(list1):
    
    def check(l=[list1], j=0):
        if j==len(list1)-1:
            return l     
        v=l[:]
        for i in v:
            for k in range(j+1, len(i)):
                list2=i[:]
                list2[j], list2[k]=list2[k], list2[j]
                l.append(list2)
        return check(l, j+1)   
    return check()

