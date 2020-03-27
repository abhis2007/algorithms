def near_power(n):
    count=0
    val=2
    if(n==1):
        return val
    while(1):
        n//=2
        count+=1
        val*=count
        if(n==1):
            break
    return val
def buildtree(lists,index,start,end):
    if(start>end):
        return
    elif(start==end):#base case
        tree[index]=lists[start]
        sums[index]=lists[start]
    else:
        mid=(start+end)//2
        #left subtree
        buildtree(lists,2*index,start,mid)
        #right subtree
        buildtree(lists,2*index+1,mid+1,end)
        #query  
        tree[index]=min(tree[index*2],tree[2*index+1])
        sums[index]=(tree[index*2]+tree[2*index+1])

lists=list(map(int,input().split()))
p=near_power(len(lists))
#for more detail refer utube channel-coding block(range min query)
#and go through geek for geeks article for calculation of maximum length of tree link:-
#https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/
#go through all three articles
print(p*4)
tree=[0 for i in range(p*4)]
sums=[0 for i in range(p*4)]
buildtree(lists,1,0,len(lists)-1)
print(tree)
print(sums)
