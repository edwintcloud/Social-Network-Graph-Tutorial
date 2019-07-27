from faker import Faker
import sys
import random
from graph import Graph
import networkx as nx
import matplotlib.pyplot as plt

def generate_names(n = 9, f_name = "names.txt"):
    fake = Faker()
    with open(f_name, "w") as f:
        for _ in range(int(n)):
            f.write(f"{fake.name()}\n")

def generate_graph(your_name, names_file="names.txt", f_name="graph_data.txt"):
    with open(f_name, "w") as f:
        # write graph type
        f.write("G\n")
        # get list of friend names
        with open(names_file, "r") as f2:
            friends = f2.read().splitlines()
        # write vertices
        f.write(f"{your_name},{','.join(friends)}\n")
        # iterate through friends
        for friend in friends:
            # edge from you to the friend
            f.write(f"({your_name},{friend})\n")
            # create a copy of friends without current friend
            other_friends = [i for i in friends if i != friend]
            # generate a random sample of 2-4 other friends
            idx_sample = random.sample(range(len(other_friends)), random.randint(2, 4))
            # edge from friend to 2-4 other distinct friends
            for idx in idx_sample:
                f.write(f"({friend},{other_friends[idx]})\n")

def draw_graph(graph_file="graph_data.txt", f_name="social_path.png"):
    # create graph from file
    g = Graph(graph_file)
    # create nx graph with edges
    nxGraph = nx.DiGraph(g.get_edges())
    plt.figure(1,figsize=(12,9))
    plt.margins(0.1)
    # draw graph
    nx.draw_shell(nxGraph, with_labels=True, node_size=9000, font_size=10, width=1.4, font_color='w')
    
    # save to png
    plt.savefig(f_name)
    # display on screen
    plt.show()

if __name__ == "__main__":
    if sys.argv[1] == 'generate_names':
        generate_names(*sys.argv[2:])
    elif sys.argv[1] == 'generate_graph':
        generate_graph(sys.argv[2], *sys.argv[3:])
    elif sys.argv[1] == 'draw_graph':
        draw_graph(*sys.argv[2:])