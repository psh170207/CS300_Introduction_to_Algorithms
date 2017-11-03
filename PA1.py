# 2017 Spring CS300 Programming Assignment #1
# Due: 2017.10.17 11:59 PM
# TA in charge of PA1: InJae YU (myhome9830@kaist.ac.kr)


import elice_utils

import networkx as nx
import operator
import math
import heapq

def SCC(G):
    G_r = G.reverse()
    #========================================================
    # Implement  function SCC()
    # Construct each component using 'frozenset'
    # Return set of frozenset
    #========================================================
    #
    def DFS(G,ordered=None):
#######################################################
        def explore(G,v,visited,pre,post,clock):
            def previsit(pre,v,clock):
                pre[v] = clock
                return clock+1

            def postvisit(post,v,clock):
                post[v] = clock
                return clock+1

            # main architecture
            visited[v] = True
            clock = previsit(pre,v,clock)
            for edge in G.edges():
                if edge[0] is v :
                    if not visited[edge[1]] :
                        ret = explore(G,edge[1],visited,pre,post,clock)
                        clock = ret['clock']
                        visited = ret['visited']
            return {'clock' : postvisit(post,v,clock), 'visited' : visited}
#########################################################
        if ordered is None :
            ordered = G.nodes()
        visited = {}
        pre = {}
        post = {}
        clock = 1
        for vertex in ordered:
            visited[vertex] = False
            pre[vertex] = 0
            post[vertex] = 0

        component_set = []
        not_visited = list(ordered)

        for vertex in ordered:
            if not visited[vertex]:
                ret = explore(G,vertex,visited,pre,post,clock)
                clock = ret['clock']
                visited = ret['visited']

                distinct_component=[]
                for v in not_visited:
                    if visited[v] is True:
                        distinct_component+=[v]

                for v in list(ordered):
                    if visited[v] is True and v in not_visited:
                        not_visited.remove(v)

                component_set.append(distinct_component)

        return {'pre':pre,'post':post,'component_set' : component_set}

    post_r = DFS(G_r)['post']
    postnum_ordered = dict(sorted(post_r.items(), key = operator.itemgetter(1))).keys()
    ordered_vertex = list(postnum_ordered)
    ordered_vertex.reverse()

    scc_component = DFS(G,ordered_vertex)['component_set']

    frozen_component = []
    for scc in scc_component:
        frozen_component.append(frozenset(scc))

    components = set(frozen_component)
    return components

def find_path(source, destination):
    G = city_initialize()
    #========================================================
    # Implement  function find_path()
    #========================================================
    def decreasekey(H,v):
        idx = 0
        for i in range(len(list(H))):
            if H[i][1] is v :
                idx = i
        H[idx] = H[-1]
        heapq.heappop(H)
        heapq.heappush(H,[dist[v],v])
        heapq.heapify(list(H))
        return H

    path = []
    d = 0
    dist = {}
    prev = {}

    for v in G.nodes():
        dist[v] = math.inf
        prev[v] = None
    dist[source] = 0

    H = []
    for v in G.nodes():
        H.append([dist[v],v])

    l = nx.get_edge_attributes(G,'distance')
    heapq.heapify(H)
    while len(list(H)) is not 0 :
        u = heapq.heappop(H)[1]
        for e in G.edges():
            if e[0] is u :
                print(l[e])
                if dist[e[1]] > dist[u] + l[e]:
                    dist[e[1]] = dist[u] + l[e]
                    prev[e[1]] = u
                    H = decreasekey(H,e[1])
    d = dist[destination]
    if d is not math.inf:
        s = destination
        while s is not source :
            path.append(s)
            s = prev[s]
        path.append(source)
        return (d,path)
    else:
        return (0,[])

#============================================================
# WARNING
# DO NOT MODIFY THE CODE BELOW
#============================================================

def build_graph(filename):
    G = nx.DiGraph()
    f = open('DirectedGraph.txt', 'r')
    #line = f.readline()
    while True:
        line = f.readline()
        if not line: break
        v1, v2 = str.split(line)
        G.add_edge(v1, v2)
    f.close()
    #you can use below lines to visualize graph in your IDE(not elice)
    #nx.draw_circular(G)
    #plt.show()
    return G

def city_initialize():
    global G
    G = nx.Graph()
    global cities, distance
    cities = ['cheorwon','yeoncheon','sokcho','yangyang','gimpo','seoul','incheon','gangneung','yongin','wonju','taebaek','yeongju','uljin','goesan','andong','gongju','daejeon','pohang','jeonju','daegu','cheongdo','ulsan','gwangju','gurye','gimhae','hampyeong','gwangyang','busan','sinan','jindo','goheung','yeosu']
    distance = [[-1,22,110,-1,-1,71,-1,-1,105,110,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [22,-1,-1,-1,69,60,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [110,-1,-1,16,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,16,-1,-1,-1,-1,45,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,69,-1,-1,-1,-1,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [71,60,-1,-1,24,-1,28,-1,41,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,18,28,-1,-1,50,-1,-1,-1,-1,-1,-1,123,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,45,-1,-1,-1,-1,-1,-1,67,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [105,-1,-1,-1,-1,41,50,-1,-1,71,-1,-1,-1,75,-1,88,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [110,-1,-1,-1,-1,-1,-1,-1,71,-1,103,93,-1,60,-1,-1,125,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,67,-1,103,-1,53,42,-1,70,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,93,53,-1,77,76,29,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,42,77,-1,-1,78,-1,-1,113,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,75,60,-1,76,-1,-1,91,-1,65,-1,-1,130,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,70,29,78,91,-1,-1,125,84,-1,80,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,123,-1,88,-1,-1,-1,-1,-1,-1,-1,26,-1,71,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,104,125,-1,-1,-1,65,125,26,-1,-1,64,125,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,113,-1,84,-1,-1,-1,-1,70,70,55,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,71,64,-1,-1,131,149,-1,81,77,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,130,80,-1,125,70,131,-1,29,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,70,149,29,-1,55,-1,128,49,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,55,-1,-1,55,-1,-1,-1,52,-1,-1,47,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,81,-1,-1,-1,-1,56,-1,33,-1,-1,-1,-1,75,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,77,-1,128,-1,56,-1,134,-1,38,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,49,52,-1,134,-1,-1,119,18,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,33,-1,-1,-1,-1,-1,-1,70,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,38,119,-1,-1,-1,-1,-1,62,21],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,47,-1,-1,18,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,28,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,70,-1,-1,28,-1,98,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,75,-1,-1,-1,62,-1,-1,98,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,21,-1,-1,-1,-1,-1]]
    i=0
    for v in cities:
        G.add_node(v)
        i=i+1
    for i in range(len(cities)):
        for j in range(len(cities)):
            if(distance[i][j] !=-1):
                G.add_edge(cities[i],cities[j],distance=distance[i][j])
    return G

if __name__ == '__main__':
    SCC(build_graph('DirectedGraph.txt'))
    print(find_path('cheorwon', 'jindo'))
