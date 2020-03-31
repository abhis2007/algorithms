def min_query(lists,index,lists_s,lists_e,query_s,query_e):
    #NO OVERLAP
    if(lists_s>query_e or query_s>lists_e):
        return 1888888
    #COMPLETE OVERLAP
    if(query_s<=lists_s and query_e>=lists_e):
        return tree[index]
    #PARTIAL OVERLAP CALL FUNCTION BOTH SIDE
    mid=(lists_s+lists_e)//2
    left=min_query(lists,2*index,lists_s,mid,query_s,query_e)
    right=min_query(lists,2*index+1,mid+1,lists_e,query_s,query_e)
    return min(right,left)

def near_power(n):
    val=1
    if(n==1):
        return val
    while(1):
        n//=2
        val*=2
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
print(p)
tree=[0 for i in range(p*4)]
sums=[0 for i in range(p*4)]
buildtree(lists,1,0,len(lists)-1)
print(tree)
print(sums)
while(1):
    a=int(input())
    b=int(input())
    print(min_query(lists,1,0,len(lists)-1,a,b))
   
