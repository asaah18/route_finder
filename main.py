from data_structure import Graph, Stack, Queue
from json_reader import read_json_file


def get_user_choice(choices) -> int:
    """
    ask the user to choose from the given choices

    :param choices : list of choices as a string
    :return index_of_user_input: int
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
    graph = Graph()
    map_file_path = "macca_map.json"

    def __init__(self):
        self.setup_graph()

    def setup_graph(self):
        print("read map file")
        # read map from json file
        macca_map = read_json_file(self.map_file_path)
        # insert into graph
        print("setup graph...")
        for node, connected_nodes in macca_map.items():
            self.graph.add_node(node, connected_nodes)
            # print("add ", node, "which is connected to:", connected_nodes)
        print("finished setup graph")
        # print(self.graph.get_all_nodes())

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
        self.depth_first_search()
        print("=" * 25, "\n", "end of DFS", "=" * 25)
        self.breadth_first_search()

    def depth_first_search(self):
        """travel form start_place to target_place from left to right while logging the traveled cities"""
        visited_places = []
        print("----------Depth First Search Traverse-------------")
        self.stack.unique_push(self.start_place)

        while not self.stack.is_empty():
            current_place = self.stack.pop()
            visited_places.append(current_place)
            print("I am at", current_place, "place")
            self.stack.display()
            print("Visited cities are:", visited_places)
            if current_place is self.target_place:
                print("I have reached the target place")
                break
            else:
                connected_nodes = self.meccaMap.graph.get_children_of_node(current_place)

                print("The connected nodes are:")
                print()
                for node in connected_nodes:
                    for key, value in node.items():
                        print(key, ': ', value)
                    print()

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
        visited_places = []
        print("----------Breadth First Search Traverse-------------")
        self.queue.unique_enqueue(self.start_place)

        while not self.queue.is_empty():
            current_place = self.queue.dequeue()
            visited_places.append(current_place)
            print("I am at", current_place, "place")
            self.queue.display()
            print("Visited places are:", visited_places)
            if current_place is self.target_place:
                print("I have reached the target place")
                break
            else:
                connected_nodes = self.meccaMap.graph.get_children_of_node(current_place)

                print("The connected nodes are:")
                print()
                for node in connected_nodes:
                    for key, value in node.items():
                        print(key, ': ', value)
                    print()

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


FindRoute()
