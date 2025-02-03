# Markov Chain graph. Project adapted from freecodecamp.
""" Markov Chain is basically a mathematical probabilistic model
in which the current state is determined by the the previous one.
We used this model to generate text. By adding a weight to each word
that we found in a sample text, we can determine the most likely
succession of words.
"""
# this is our Markov Chain representation
# define the graph in terms of vertices
class Vertex:
    def __init__(self, value):
        self.value = value # value is just the word!!!
        self.adjacent = {} # keys are the adjacent vertices, values are its weights.
        # for easily accessing to an adjacent vertex weight (e.g., for weight incrementation)

    # add an edge (a connection) to a vertex
    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    # increment the weight of the edge in vertex
    # (since it defaults to '0' if 'vertex' is not found
    # it can create a new vertex with of weight = 1)
    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1 # actually it should have been: self.adjacent.get(vertex) + 1, but we don't want an accidental error to occur

    def get_adjacent_words_and_weights(self):
        return [(vertex.value, weight) for vertex, weight in self.adjacent.items()]

from random import choice
# create a graph for storing those vertices
# the graph is an important data structure for this project since it will allow us to have in a unique container all the words we process.
class Graph:
    def __init__(self):
        self.vertices = {} # key is the word, value is the Vertex object

    # return all the words
    def get_words(self):
        return self.vertices.keys()

    # for contructing the graph
    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)
        return self.vertices[value]

    # search for a vertex in the graph given the word
    def get_vertex(self, value):
        return self.vertices.get(value, None)

    # search for a vertex in the graph given the word (for users)
    def get_vertex_user(self, value):
        vertex = self.vertices.get(value, None)
        if vertex: # if the value/word is associated to a vertex we simply return the vertex object
            return vertex
        # otherwise we ask for the user input to know if the creation of a new vertex is desired
        i = 0
        while True:
            answer = input(f"The value {value} isn't associated with a vertex. \
                           \nDo you want to create a new vertex with this word? (y/n): \
                           \n")
            if answer == "n":
                return
            elif answer == "y":
                break
            else:
                print("That isn't a valid input. Please, try it again.")
            if i == 10:
                return
            i += 1
        # if the user chooses to create a new vertex with the entered value 
        self.add_vertex(value)
        vertex = self.vertices[value]
        return vertex            

    # search for the most probable word linked to the current word or to the current vertex
    def get_next_word(self, word, vertex=None):
        # print(word)
        current_value = word
        current_vertex = vertex
        # if the vertex wasn't provided as input
        if current_value and current_vertex is None: # search for the corresponding vertex value the vertex 
            current_vertex = self.get_vertex(current_value) # with our previously defined method
        # once we have the vertex, we need to check which of its adjacents vertices has the greatest value (i.e., the greatest weight). That would be the most probable word to be next
        # print(word)
        if current_vertex: # We check if there's a current_vertex bcuz it exists the possibility that the user has entered a wrong word and doesn't want to add it
            if list(current_vertex.adjacent):
                greatest_weight = -1 # remember the weights are initialized with 0 as weight
                for word, weight in current_vertex.adjacent.items():
                    if weight > greatest_weight:
                        probable_word = word
                del current_vertex.adjacent[probable_word] # destructively iterate over the dictionary to avoid word repetition in the composition
                return probable_word
            else:# if a word adjacent dictionary gets empty
                return self.vertices[choice(list(self.vertices))] # set a random word to continue the composition. This will cause the determinism to be lost, but we don't want to complicate more this project
        # if the word entered wasn't in the graph
        if input(f"We couldn't find the word '{current_value}' in the graph. Would you like to try with another word? (y/n):\n") == "y":
            word = input("Type the word: ")
            return self.get_next_word(word)
            # print(word)