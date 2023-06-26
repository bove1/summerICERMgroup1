import numpy as np
from graphsOfInterest import *

g = graphFormat(kn92)
print(g)

def numSpanningTrees(g):
    size = max(max(a) for a in g) + 1
    laplacian = [[0 for i in range(size)] for i in range(size)]
    for i, j in g:
        laplacian[i][j] -= 1
        laplacian[j][i] -= 1
        laplacian[i][i] += 1
        laplacian[j][j] += 1
    # print(np.array(laplacian, dtype=int))
    redLaplace = np.array(laplacian, dtype=int)[:size - 1, :size - 1]
    return int(np.rint(np.linalg.det(redLaplace)))

def nonMatch(g):
    matches = []
    for i in g:
        for j in g:
            if i[0] != j[0] and i[0] != j[1] and i[1] != j[0] and i[1] != j[1]:
                g_copy = g.copy()
                g_copy.remove(i)
                g_copy.remove(j)
                g_copy.append((i[0], j[1]))
                g_copy.append((i[1], j[0]))
                if numSpanningTrees(g) == numSpanningTrees(g_copy):
                    matches.append((i, j))
                g_copy = g.copy()
                g_copy.remove(i)
                g_copy.remove(j)
                g_copy.append((i[0], j[0]))
                g_copy.append((i[1], j[1]))
                if numSpanningTrees(g) == numSpanningTrees(g_copy):
                    matches.append((i, (j[1], j[0])))  
    return matches

print(numSpanningTrees(g))
print(nonMatch(g))