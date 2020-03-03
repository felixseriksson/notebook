#myfunctions.py innehåller olika funktioner som kan vara användbara i olika sammanhang
#def funktionsnamn():
#   gör nånting
#   return nåt annat
#För att importera: "import myfunctions" eller "from myfunctions import funktionsnamn"
###-----------------------------------------------------------------------------------------------
def testing():
    print("Hello world!")
###-----------------------------------------------------------------------------------------------

def dictswitch(dictionary):
    tempdict = {dictionary[k]:k for k in dictionary}
    return tempdict
###-----------------------------------------------------------------------------------------------

from collections import defaultdict
from heapq import heapify, heappop, heappush

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")

def makereadable(foundpath):
    # tar in input direkt från djikstras
    path = []
    for n in str(foundpath):
        if n.isalnum():
            path.append(n)
    lengthofpath = path.pop(0)
    return lengthofpath, reversed(path)
    # returnerar längden på kortaste stigen, en lista med noderna i den kortaste stigen som strings

# graphen görs av en kantlista där varje entry är en tuple på formen (från, till, vikt)
# där alltså från och till kan vara ints eller strings men vikt är en int
edges = [
        ("A", "B", 1),
        ("B", "C", 1),
        ("C", "A", 1),
        #("A", "B", 5)
    ]

# output ges på formen (vikt, (sista noden,(näst sista noden,(...,(första noden,())))))
print(edges)
res = dijkstra(edges, "A", "C")
print(res)
print(makereadable(res))
###-----------------------------------------------------------------------------------------------

class Node:
    '''
    A simple node class which stores rank and parent, for use in Disjoint Sets.
    By default, the parent is set to itself, unless a new parent is added.
    '''
    def __init__(self, rnk, d):
        self.rank = rnk
        self.parent = self
        self.data = d
        self.size = 1


class DisjointSet:
    '''
    A disjoint set datastructure, for implementing union find operations.
    '''

    def __init__(self):
        # The members dictionary hashes the value to the corresponding node
        self.members = dict()

    '''
    Input: Value to be retrieved from sets.
    Output: Node corresponding to the value if it is present, None otherwise.
    '''
    def get(self, val):
        if val in self.members:
            return self.members[val]
        else:
            return None

    def make_set(self, val):
        if val not in self.members:
            # The rank is initially 0 since it is a new set
            self.members[val] = Node(0, val)

    '''
    Takes input of a given node in the members dictionary.
    Returns the root of its set.
    '''
    def find(self, n):
        if n.parent != n:
            self.members[n.data].parent = self.find(n.parent)
        return n.parent

    def union(self, n1, n2):
        root_n1 = self.find(n1)
        root_n2 = self.find(n2)

        if root_n1 == root_n2:
            return True
        else:
            if root_n1.rank > root_n2.rank:
                self.members[root_n1.data].size += self.members[root_n2.data].size
                self.members[root_n2.data].parent = self.members[root_n1.data]
            elif root_n1.rank < root_n2.rank:
                self.members[root_n2.data].size += self.members[root_n1.data].size
                self.members[root_n1.data].parent = self.members[root_n2.data]
            else:
                self.members[root_n1.data].size += self.members[root_n2.data].size
                self.members[root_n2.data].parent = self.members[root_n1.data]
                self.members[root_n1.data].rank = root_n1.rank+1