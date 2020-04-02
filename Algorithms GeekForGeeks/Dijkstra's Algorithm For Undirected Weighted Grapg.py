import math
def findMinVertex(path_distance,visited,n,source):
    minVertex=source
    for i in range(n):
        if(not(visited[i]) and path_distance[i]<=path_distance[minVertex]):
            minVertex=i
    return minVertex
        
def dijkastra(edges,n,path_distance,visited):
    source=int(input())
    path_distance[source]=0
    for j in range(n):
        minVertex=findMinVertex(path_distance,visited,n,source)
        visited[minVertex]=True
        minimum=[math.inf]*n
        for i in range(n):
            w=edges[minVertex][i]
            if(w>0 and (not(visited[i]))):
                dist=path_distance[minVertex]+w
                if(path_distance[i]>dist):
                    path_distance[i]=dist
                    minimum[i]=dist
        source=minimum.index(min(minimum))  
               
n,e=map(int,input().split())
lists=[]
edges=[]
visited=[]
path_distance=[]
for i in range(n):
    path_distance.append(math.inf)
    visited.append(False)
    lists=[]
    for j in range(n):
        lists.append(0)
    edges.append(lists)
for i in range(e):
    first_vertex,second_vertex,edge_weight=map(int,input().split())
    edges[first_vertex][second_vertex]=edge_weight
    edges[second_vertex][first_vertex]=edge_weight
    
dijkastra(edges,n,path_distance,visited)
for i in range(n):
    print(i,,path_distance[i])
    
