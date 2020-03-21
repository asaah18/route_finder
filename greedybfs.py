from heapq import heappop as pop, heappush as push


class GBFS:
    def __init__(self):
        # item (node:parent)
        self.visited = {}
        self.path = []

    def traverser(self, graph, source, dest):
        queue = []
        start_heuristic = float(graph.node[source]['heuristic'])
        # Queue item (heuristic, (node, cost, parent))
        push(queue, (start_heuristic, (source, 0, None)))

        while queue:
            print(queue)
            currentnode, cost, parent=pop(queue)[1]
            print(currentnode)
            # goal check
            if(currentnode == dest):
                self.visited[currentnode]=parent
                self.path=[currentnode]
                origin = parent
                while origin is not None:
                    self.path.append(origin)
                    origin=self.visited[origin]
                self.path.reverse()
                break

            if(currentnode not in list(self.visited.keys())):
                self.visited[currentnode]=parent
  
            # check neighbours
            # Items returns (neighbornode, {dict of edge attributes})
            for neighbor, data in graph[currentnode].items():
                nheuristic= float(graph.node[neighbor]['heuristic'])
                ncost= cost + float(data['weight'])
                #  creating list with nodes in the queue
                queuenodes=[tuple[1][0] for tuple in queue]
                if(neighbor not in list(self.visited.keys()) and neighbor not in queuenodes):
                    # push to the queue with heuristic, cost ,parent
                    push(queue,(nheuristic, (neighbor,ncost,currentnode)))


