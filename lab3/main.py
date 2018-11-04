class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.connection = []


class Graph:
    def __init__(self):
        self.vertices = []

    #creating connections in two directions (f/ex: 1->2; 2->1)
    def add_connection(self, vertex1, vertex2):

        counter = 0
        for i in self.vertices:
            if i.vertex == vertex1.vertex:
                vertex1 = self.vertices.pop(counter)
            counter += 1

        counter = 0
        for i in self.vertices:
            if i.vertex == vertex2.vertex:
                vertex2 = self.vertices.pop(counter)
            counter += 1

        vertex1.connection.append(vertex2)
        vertex2.connection.append(vertex1)
        self.vertices.append(vertex1)
        self.vertices.append(vertex2)

    def get_man_list(self):
        list = []
        for vertex in self.vertices:
            if int(vertex.vertex) % 2 == 1:
                list.append(vertex)
        return list

    def get_woman_list(self):
        list = []
        for vertex in self.vertices:
            if int(vertex.vertex) % 2 == 0:
                list.append(vertex)
        return list

    #bfs
    def is_connected(self, start_v, search_v):
        visited = {vertex: False for vertex in self.vertices} #marking all the vertices as not visited
        queue = [] #creating a queue for bfs
        queue.append(start_v) #marking first vertex as visited
        visited[start_v] = True

        while queue:
            current = queue.pop(0) #removing vertex from queue

            if (current.vertex == search_v.vertex): #checking if current vertex is a 'goal' node
                return True
            else:
                for i in current.connection: #all current's children i
                    if visited.get(i) == False: #that wasnt visited
                        queue.append(i) #adding them to the end of the queue
                        visited[i] = True  #and marking as visited

        return False


graph = Graph()

values = open('wedd.txt', 'r')
readable_values = values.readlines()
for line in readable_values:
    line = line.strip('\n')
    values_array = line.split(',')
    graph.add_connection(Vertex(values_array[0]), Vertex(values_array[1]))

wedd_couples = set()
for vertex1 in graph.get_man_list():
    for vertex2 in graph.get_woman_list():
        if graph.is_connected(vertex1, vertex2):
            continue
        else:
            str = vertex1.vertex + "/" + vertex2.vertex
            wedd_couples.add(str)
print(wedd_couples.__len__())
print(wedd_couples)