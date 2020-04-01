def display(edges,n,start_vertex,visited):
    print(start_vertex)
    visited[start_vertex]=True
    for i in range(n):
        if(edges[start_vertex][i]==1 and not (visited[i])):
            display(edges,n,i,visited)

n,e=map(int,input().split())
edges=[]
lists=[]
visited=[]
for i in range(n):
    lists=[]
    visited.append(False)
    for j in range(n):
        lists.append(0)
    edges.append(lists)
print(edges)
for i in range(e):
    first_vertex,second_vertex=map(int,input().split())
    edges[first_vertex][second_vertex]=1 
    edges[second_vertex][first_vertex]=1
    print(edges)
start_vertex=0
print(edges)
display(edges,n,start_vertex,visited)
