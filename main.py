# No code from the web has been used, every line has been writting by the students

from data_structure import Graph, Stack, Queue
import json , time

steps = []
times = []

def get_user_choice(choices):
    """
    ask the user to choose from the given choices
    """

    # print choices
    for index, choice in enumerate(choices):
        print("[" + str(index) + "] " + choice)
    # get user input
    while True:
        user_input = input("\n" + "input: ")
        if (user_input.isdigit() is False) or (int(user_input) not in range(len(choices))):
            print("wrong input!")
        else:
            return int(user_input)


class MaccaMap:
    def __init__(self):
        self.graph = Graph(json.loads(open('mecca-map.json').read()))
    
    def set_starting_place(self):
        """set the starting place as a string"""
        cities = self.graph.get_all_nodes()
        print("Choose a place number to start with:" + "\n")
        # start_place = cities[get_user_choice(cities)]
        start_place = cities[0]
        print("you will start at", start_place, "place")
        return start_place

    def set_target_place(self):
        """set the starting place as a string"""
        cities = self.graph.get_all_nodes()
        print("Choose a place number as a target:" + "\n")
        # start_place = cities[get_user_choice(cities)]
        target_place = cities[1]
        print("your target place is", target_place, "place")
        return target_place


class FindRoute:
    """a class to find route between 2 cities using depth first search"""
    
    def __init__(self):
        self.stack = Stack()
        self.queue = Queue()
        self.meccaMap = MaccaMap()
        self.start_place = self.meccaMap.set_starting_place()
        self.target_place = self.meccaMap.set_target_place()
    
    def printNodes(self, queue):
        print('-------------- Nodes --------------')
        print()
        for node in queue:
            print(node['name'], ', ')
        print()


    def depth_first_search(self):
        """travel form start_place to target_place from left to right while logging the traveled cities"""
        global steps ,times
        current_step = 0
        time0 = time.time()

        visited_places = []
        print("----------Depth First Search Traverse-------------")
        self.stack.unique_push(self.start_place)

        while not self.stack.is_empty():
            current_step+=1
            current_place = self.stack.pop()
            visited_places.append(current_place)
            print("I am at", current_place, "place")
            self.stack.display()
            print("Visited cities are:", visited_places)
            if current_place == self.target_place:
                print("I have reached the target place")

                time1 = time.time()
                time_differnce = time1 - time0
                times.append(time_differnce)
                steps.append(current_step)

                break
            else:
                connected_nodes = self.meccaMap.graph.get_children_of_node(
                    current_place)

                print("The connected nodes are:")
                print()
                self.printNodes(connected_nodes)
                for node in connected_nodes:
                    # push to stack if not visited and not in stack
                    if node['name'] not in visited_places:
                        self.stack.unique_push(node['name'])
                        # print(node, "has been added to stack")

                self.stack.display()
            print("-----------------------------------------")
        else:
            # executed if target not found(break statement not executed)
            print("I wasn't able to find a route")

    def breadth_first_search(self):
        """travel form start_place to target_place from left to right breadth first while logging the traveled cities"""
        global steps , times
        current_step = 0
        time0 = time.time()

        visited_places = []
        print("----------Breadth First Search Traverse-------------")
        self.queue.unique_enqueue(self.start_place)

        while not self.queue.is_empty():
            current_step+=1
            current_place = self.queue.dequeue()
            visited_places.append(current_place)
            print("I am at", current_place, "place")
            self.queue.display()
            print("Visited places are:", visited_places)
            if current_place == self.target_place:
                print("I have reached the target place")

                time1 = time.time()
                time_differnce = time1 - time0
                times.append(time_differnce)
                steps.append(current_step)

                break
            else:
                connected_nodes = self.meccaMap.graph.get_children_of_node(
                    current_place)

                print("The connected nodes are:")
                print()
                self.printNodes(connected_nodes)
                
                for node in connected_nodes:
                    # push to stack if not visited and not in stack
                    if node['name'] not in visited_places:
                        self.queue.unique_enqueue(node['name'])
                        # print(node, "has been added to stack")

                self.queue.display()
            print("-----------------------------------------")
        else:
            # executed if target not found(break statement not executed)
            print("I wasn't able to find a route")

    def greedy_first_search(self):
        global steps , times
        current_step = 0
        time0 = time.time()

        visited = complate_path =['']
        current_place = visited[0] = complate_path[0] = self.start_place
        
        while current_place is not self.target_place:
            connected_nodes = self.meccaMap.graph.get_children_of_node(
                current_place)
            queue = sorted(connected_nodes, key=lambda i: i['distance'])
            self.printNodes(queue)
            for place in queue:
                current_step+=1
                first_in_queue = queue.pop(0)['name']
                print('remove ', first_in_queue, 'from queue..')
                print()
                
                # connected nodes to the first element in queue which we just pop-ed up
                connected_nodes_to_first = sorted(self.meccaMap.graph.get_children_of_node(first_in_queue), key=lambda i: i['distance'])
                
                for place in connected_nodes_to_first:
                    if place['name'] == self.target_place:
                        complate_path.append(first_in_queue)
                        complate_path.append(place['name'])
                        print("I have reached the target place")
                        
                        time1 = time.time()
                        time_differnce = time1 - time0
                        times.append(time_differnce)
                        steps.append(current_step)
                        
                        return complate_path
                    
                # connected nodes to the first element in queue which we just pop-ed up, but filtered from visited places to add them to the queue
                connected_nodes_filtered = [i for i in connected_nodes_to_first if i['name'] not in visited] 
                    
                queue.extend(connected_nodes_filtered)
                self.printNodes(queue)

        # print("="*25, "\n", "end of DFS", "="*25)
        # print("="*25, "\n", "end of DFS", "="*25)
        # print("="*25, "\n", "end of DFS", "="*25)

FindRoute().depth_first_search()
print("="*25, "\n", "end of DFS", "="*25)
FindRoute().breadth_first_search()
print("="*25, "\n", "end of BFS", "="*25) 


complate_path = FindRoute().greedy_first_search()
print()
print('complate path: ')


print(*complate_path, sep=" -> ")

print()
print("DFS took ", steps[0] ," steps, and " ,times[0]," seconds to complete")
print("BFS took ", steps[1] ," steps, and " ,times[1]," seconds to complete")
print("GFS took ", steps[2] ," steps, and " ,times[2]," seconds to complete")
