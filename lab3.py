matr = [
         [0, 2, -1, 3, 8, -1, -1, -1],
         [2, 0, 1, -1, -1, 9, -1, -1],
         [-1, 1, 0, -1, -1, 4, -1, 3],
         [3, -1, -1, 0, 1, -1, 3, -1],
         [8, -1, -1, 1, 0, -1, 9, 10],
         [-1, 9, 4, -1, -1, 0, -1, 6],
         [-1, -1, -1, 3, 9, -1, 0, 10],
         [-1, -1, 3, -1, 10, 6, 10, 0],
       ]
#prima's
def search_min(tr, vizited):
    min=max(tr)
    for ind in vizited:
        for index, elem in enumerate(tr[ind]):
            if elem>0 and elem<min and index not in vizited:
                min=elem
                index2=index
    return [min, index2]

def prim(matr):
    toVisit=[i for i in range(1,len(matr))]
    vizited=[0]
    result=[0]
    for index in toVisit:
        weight, ind=search_min(matr, vizited)
        result.append(weight)
        vizited.append(ind)
    return result

print(prim(matr))



#kruskal's
N, M = map(int, input().split())
Edges = []
for i in range(M):
    start, end, weight = map(int, input().split())
    Edges.append([weight, start, end])
Edges.sort()
Comp = [i for i in range(N)]
Ans = 0
for weight, start, end in Edges:
    if Comp[start] != Comp[end]:
        Ans += weight
        a = Comp[start]
        b = Comp[end]
        for i in range(N):
            if Comp[i] == b:
                Comp[i] = a