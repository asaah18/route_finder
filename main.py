from data_structure import Graph, Stack, Queue


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
    def __init__(self):
        self.graph = Graph()
        self.setup_graph()

    def setup_graph(self):
        self.graph.add_node("Kaaba", [
            {
                'name': "Al-Marwah",
                'distance': 310
            },
            {
                'name': "Al-Safa",
                'distance': 140
            },
            {
                'name': "King AbdulAziz Gate",
                'distance': 100
            },
            {
                'name': "Tawsaat King Fahad",
                'distance': 182
            }])

        self.graph.add_node("Al-Marwah", [
            {
                'name': "Kaaba",
                'distance': 310
            },
            {
                'name': "Macca Library",
                'distance': 280
            },
            {
                'name': "Al-Safa",
                'distance': 370
            }])

        self.graph.add_node("Al Salam Gate", [
            {
                'name': "Al-Safa",
                'distance': 90
            },
            {
                'name': "Macca Library",
                'distance': 320
            }])

        self.graph.add_node("Al-Safa", [
            {
                'name': "Kaaba",
                'distance': 140
            },
            {
                'name': "Al-Marwah",
                'distance': 370
            },
            {
                'name': "Al Salam Gate",
                'distance': 90
            },
            {
                'name': "King AbdulAziz Gate",
                'distance': 170
            }
        ])

        self.graph.add_node("King AbdulAziz Gate", [
            {
                'name': "Kaaba",
                'distance': 100
            },
            {
                'name': "Al-Safa",
                'distance': 170
            },
            {
                'name': "Al-Safwa Hotel",
                'distance': 200
            },
            {
                'name': "AlWaqf",
                'distance': 215
            }
        ])

        self.graph.add_node("Al-Safwa Hotel", [
            {
                'name': "King AbdulAziz Gate",
                'distance': 200
            },
            {
                'name': "AlHaramain Administration",
                'distance': 225
            },
            {
                'name': "AlWaqf",
                'distance': 130
            }
        ])

        self.graph.add_node("AlWaqf", [
            {
                'name': "King AbdulAziz Gate",
                'distance': 130
            },
            {
                'name': "Al-Safwa Hotel",
                'distance': 130
            },
        ])

        self.graph.add_node("AlHaramain Administration", [
            {
                'name': "Al-Safwa Hotel",
                'distance': 225
            },
        ])

        self.graph.add_node("Tawsaat King Fahad", [
            {
                'name': "Kaaba",
                'distance': 182
            },
            {
                'name': "Abraj Maccah",
                'distance': 120
            },
            {
                'name': "Dar Al-Tawheed",
                'distance': 135
            },
            {
                'name': "Tawsaat King Abdullah",
                'distance': 220
            }
        ])

        self.graph.add_node("Abraj Maccah", [
            {
                'name': "Tawsaat King Fahad",
                'distance': 120
            },
            {
                'name': "Dar Al-Tawheed",
                'distance': 150
            },
        ])

        self.graph.add_node("Dar Al-Tawheed", [
            {
                'name': "Tawsaat King Fahad",
                'distance': 135
            },
            {
                'name': "Abraj Maccah",
                'distance': 150
            },
            {
                'name': "Jabal Omar",
                'distance': 350
            }
        ])

        self.graph.add_node("Tawsaat King Abdullah", [
            {
                'name': "Jabal Alkaaba",
                'distance': 550
            },
            {
                'name': "Tawsaat King Fahad",
                'distance': 220
            },
            {
                'name': "Jabal Omar",
                'distance': 450
            }
        ])

        self.graph.add_node("Jabal Omar", [
            {
                'name': "Dar Al-Tawheed",
                'distance': 350
            },
            {
                'name': "Tawsaat King Abdullah",
                'distance': 450
            }
        ])

        self.graph.add_node("Jabal Alkaaba", [
            {
                'name': "Tawsaat King Abdullah",
                'distance': 550
            }
        ])
        print("graph has been setup.")

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
        print("="*25, "\n", "end of DFS", "="*25)
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
