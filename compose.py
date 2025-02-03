# import os
from reader import get_words_from_file
from graph import Graph

# add the words to the graph
def make_graph(words):
    g = Graph()
    # first we create a vertex object and add it to our Graph Class, with the word as the value if it doesn't still exists
    previous_vertex = g.add_vertex(words[0]) # if we process only one text the first word won't be processed
    for word in words[1:]: # for each word in words, except the very first one
        curr_vertex = g.get_vertex(word) # let's check if the word is a vertex in the graph already
        if curr_vertex is None: # if it isn't
            curr_vertex = g.add_vertex(word) # we add it to our graph as a new vertex
            previous_vertex.add_edge_to(curr_vertex) # if the word wasn't a vertex in our graph, we obviously need to connect it with an edge with the previous vertex
        else: # if it's already a vertex
            if curr_vertex in previous_vertex.adjacent.keys(): # let's check if it is an edjacent vertex
                previous_vertex.increment_edge(curr_vertex)
            else:
                previous_vertex.add_edge_to(curr_vertex)
        previous_vertex = curr_vertex
    return g

def visualize_data(g, words, all_vertices=False):
    print("number of words processed:", len(words))
    print("number of words in the graph (number of unique words):", len(g.get_words()), "\n")
    if all_vertices:
        for vertex in g.vertices.values():
            print(f"'{vertex.value}':", vertex.get_adjacent_words_and_weights())
    else: # only vertices with weight greater than zero
        for vertex in g.vertices.values():
            if any(vertex.adjacent.values()):
                print(f"'{vertex.value}':", vertex.get_adjacent_words_and_weights())

def compose(g, starting_word=None, length=100):
    """
    Creates the composition from the input data based on the Markov chain model.
    Args:
        g (Graph): Graph with the data.
        starting_word (boolean): inicial word of the composition (will determine the composition itself, according to the model)
        length (int): length od the composition (length == len(compose(g).split()))
    Returns:
        string: composition based on the most likely sucession of words. If any words repeats (which will cause repetition in the composition), we go to the word with the second greatest weight, then the third and so on.
    """
    if not starting_word:
        starting_word = list(g.get_words())[0]
    
    composition = starting_word + " "
    for i in range(length-1):
        curr_word = g.get_next_word(starting_word).value
        composition += curr_word + " "
        starting_word = curr_word
        
    return composition

def main():
    text_file_path = "texts/Song of Myself (1892 version) by Walt Whitman _ Poetry Foundation.pdf"
    # text_file_path = os.path.abspath("Deep Work_ Rules for focused success in a distracted world ( PDFDrive ).pdf")
    words = get_words_from_file(text_file_path)

    g = make_graph(words)
    # visualize_data(g, words)
    print(compose(g, "myself"))
    # print(g.get_vertex("deep").get_adjacent_words_and_weights())

if __name__ == "__main__":
    main()