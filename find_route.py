import sys

from InformedSearch import InformedSearch
from UnInformedSearch import UnInformedSearch

if __name__ == '__main__':
    if sys.argv[1] == 'inf':  # reading arguments passed from cmd line
        source = sys.argv[3]
        destination = sys.argv[4]
        search_algorithm = InformedSearch(sys.argv[2], sys.argv[5])
        result = search_algorithm.a_star(source, destination)
        print 'nodes expanded: ', len(search_algorithm.fringe)
        if result is 0 or result is None:
            print 'distance: infinity'
            print 'route:'
            print 'none'
        else:
            print 'distance: ', search_algorithm.recursive_find_distance(result), ' km'
            search_algorithm.recursive_print_route(result)
    else:
        source = sys.argv[2]
        destination = sys.argv[3]
        search_algorithm = UnInformedSearch(sys.argv[1])
        result = search_algorithm.iterative_deepening_search(source, destination)
        print 'nodes expanded: ', len(search_algorithm.fringe)
        if result is 0 or result is None:
            print 'distance: infinity'
            print 'route:'
            print 'none'
        else:
            print 'distance: ', search_algorithm.recursive_find_distance(result), ' km'
            search_algorithm.recursive_print_route(result)
