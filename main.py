# written by asaah18
from data_structure import Graph, Stack


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

class FindRoute:
    """a class to find route between 2 cities using depth first search"""
    graph = Graph()
    stack = Stack()
    start_city = None
    target_city = None

    def __init__(self):
        self.setup_graph()
        self.set_starting_city()
        self.set_target_city()
        self.depth_first_search()

    def setup_graph(self):
        self.graph.add_node("Buraydah", ["Unayzah", "Riyadh-Alkhabra", "Al-Bukayriyah"])
        self.graph.add_node("Unayzah", ["AlZulfi", "Al-Badai", "Buraydah"])
        self.graph.add_node("Riyadh-Alkhabra", ["Buraydah", "Al-Badai"])
        self.graph.add_node("Al-Bukayriyah", ["Buraydah", "Sheehyah"])
        self.graph.add_node("AlZulfi", ["Unayzah", "UmSedrah"])
        self.graph.add_node("Al-Badai", ["Unayzah", "Riyadh-Alkhabra", "AlRass"])
        self.graph.add_node("Sheehyah", ["Al-Bukayriyah", "Dhalfa"])
        self.graph.add_node("UmSedrah", ["AlZulfi", "Shakra"])
        self.graph.add_node("AlRass", ["Al-Badai"])
        self.graph.add_node("Dhalfa", ["Sheehyah", "Mulaida"])
        self.graph.add_node("Shakra", ["UmSedrah"])
        self.graph.add_node("Mulaida", ["Dhalfa"])
        print("graph has been setup.")

    def set_starting_city(self):
        """set the starting city as a string"""
        cities = self.graph.get_all_nodes()
        print("Choose a city number to start with:" + "\n")
        self.start_city = cities[get_user_choice(cities)]
        print("you will start at", self.start_city, "city")

    def set_target_city(self):
        """set the starting city as a string"""
        cities = self.graph.get_all_nodes()
        print("Choose a city number as a target:" + "\n")
        self.target_city = cities[get_user_choice(cities)]
        print("your target city is", self.target_city, "city")

    def depth_first_search(self):
        """travel form start_city to target_city from left to right while logging the traveled cities"""
        visited_cities = []
        print("----------Depth First Search Traverse-------------")
        self.stack.unique_push(self.start_city)

        while not self.stack.is_empty():
            current_city = self.stack.pop()
            visited_cities.append(current_city)
            print("I am at", current_city, "city")
            self.stack.display()
            print("Visited cities are:", visited_cities)
            if current_city is self.target_city:
                print("I have reached the target city")
                break
            else:
                children_of_city = self.graph.get_children_of_node(current_city)
                print("The children cities are:", children_of_city)
                for city in children_of_city:
                    # push to stack if not visited and not in stack
                    if city not in visited_cities:
                        self.stack.unique_push(city)
                        # print(city, "has been added to stack")

                self.stack.display()
            print("-----------------------------------------")


FindRoute()
