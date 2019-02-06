import sys

from Node import Node
from ParseFileToList import ParseFileToList


class InformedSearch:

    def __init__(self, input_file, heuristic_file):
        self.closest_child = Node
        self.closest_child.f_n = sys.maxint
        self.closed = set()
        self.fringe = []
        parser = ParseFileToList(heuristic_file)
        self.heuristic_list = parser.parse_file()
        self.cities_list = parser.parse_file(input_file)

    def get_heuristic(self, city):
        for i in self.heuristic_list:
            if i[0] == city:
                return i[1]

    def create_node(self, city, distance=0, node=None):
        new_node = Node(city, distance)
        new_node.h_n = self.get_heuristic(city)
        new_node.parent = node
        new_node.f_n = int(new_node.g_n) + int(new_node.h_n)
        return new_node

    def get_children_for_node(self, node):
        children = []
        for i in self.cities_list:
            if i[0] == node.city:
                children.append(self.create_node(i[1], i[2], node))
            elif i[1] == node.city:
                children.append(self.create_node(i[0], i[2], node))
        return children

    def a_star_search(self, _source, _destination):
        node = self.create_node(_source)
        self.closed.add(_source)
        return self.recursive_astar(node, _destination)

    def recursive_astar(self, node, final_destination):
        exhausted_nodes = False
        if final_destination == node.city:
            self.fringe.append(node)
            return node
        else:
            self.fringe.append(node)
            for child in self.get_children_for_node(node):
                if self.closest_child.f_n > child.f_n:
                    self.closest_child = child
            self.closed.add(self.closest_child.city)
            result = self.recursive_astar(self.closest_child, final_destination)
            if result == -1:
                exhausted_nodes = True
            elif result != 0:
                return result
        if exhausted_nodes:
            return -1
        else:
            return 0

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

    def a_star(self, source, destination):
        for _ in (0, 15):
            result = self.a_star_search(source, destination)
            if result != -1:
                return result
