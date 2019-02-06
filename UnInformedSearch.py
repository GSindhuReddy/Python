from Node import Node
from ParseFileToList import ParseFileToList


class UnInformedSearch:
    def __init__(self, input_file):
        self.final_result = []
        self.closed = set()
        self.fringe = []
        self.route = []
        parser = ParseFileToList(input_file)
        self.cities_list = parser.parse_file()

    @staticmethod
    def create_node(city, distance, depth=0, node=None):
        new_node = Node(city, distance, depth)
        new_node.parent = node
        return new_node

    def get_children_for_node(self, node):
        children = []
        for i in self.cities_list:
            if i[0] == node.city:
                children.append(self.create_node(i[1], i[2], node.d + 1, node))
            elif i[1] == node.city:
                children.append(self.create_node(i[0], i[2], node.d + 1, node))
        return children

    def depth_limited_search(self, _source, _destination, limit):
        node = self.create_node(_source, 0)
        return self.recursive_dls(node, _destination, limit)

    def recursive_dls(self, node, final_destination, limit):
        exhausted_nodes = False
        if final_destination == node.city:
            self.fringe.append(node)
            return node
        elif node.d == limit:
            self.fringe.append(node)
            return -1
        else:
            self.closed.add(node.city)
            for current_node in self.get_children_for_node(node):
                result = self.recursive_dls(current_node, final_destination, limit)
                if result == -1:
                    exhausted_nodes = True
                elif result != 0:
                    return result
        if exhausted_nodes:
            return -1
        else:
            return 0

    def iterative_deepening_search(self, source_city, destination_city):
        for depth in range(0, 10):
            result = self.depth_limited_search(source_city, destination_city, depth)
            if result != -1:
                return result

    def recursive_print_route(self, node):
        if node.parent is not None:
            parent_city = self.recursive_print_route(node.parent)
            print parent_city, ' to ', node.city, ', ', node.g_n, 'km'
            return node.city
        return node.city

    def recursive_find_distance(self, node):
        if node.parent is not None:
            return self.recursive_find_distance(node.parent) + int(node.g_n)
        return int(node.g_n)
