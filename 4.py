
n=int(input('enter the number of rows: '))
m=int(input('enter the number of columns : '))

l=[]
for i in range(n):
    t=[]
    for j in range(m):
        t.append(int(input()))
    l.append(t)
        


#l=[[1,0,0,1,1],[1,0,0,0,1],[1,0,0,1,1],[1,1,1,1,1]]

#l=[[1,0,0,0,1],[1,1,0,1,1],[1,0,1,0,1]]


top=0

bottom=len(l)-1

right=len(l[0])-1
left=0


for i in range(len(l)//2):
    if 0 not in l[i]:
        top=top+1
    if 0 not in l[len(l)-1-i]:
        bottom=bottom-1
        
for i in range(len(l)//2):
    k=[]
    m=[]
    for j in range(len(l)//2):
         k.append(l[j][i])
         m.append(l[len(l)-1-j][i])
    if 0 not  in k:
        left=left+1
    if 0 not in m:
        right=right-1
        
        
print((top,left),(top,right),(bottom,left),(bottom,right),sep=',')          