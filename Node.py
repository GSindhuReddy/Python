class Node:
    city = None
    g_n = 0
    f_n = 0
    h_n = 0
    d = 0
    parent = None

    def __init__(self, city, distance, depth=0):
        self.city = city
        self.g_n = distance
        self.d = depth
