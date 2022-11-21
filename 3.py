def validNthnumber(target):
    validlist=[1,2,5,6,8,9]
    if target-1 < len(validlist) :
        return validlist[target-1]
    target=target-len(validlist)
    strt=9
    while target >1:
        strt=strt+1
        s=str(strt)
        for i in s:
            if int(i) not in validlist:
                break
        else:
            target=target-1
            
    return strt
        


target=int(input())

print(validNthnumber(target))