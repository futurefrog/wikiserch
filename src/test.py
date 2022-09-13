import networkx as nx
from pyvis.network import Network

net = Network(width=1920, height=1080)
class Node:
    def __init__(self, name) -> None:
        self.name = name

a = Node('A')
b = Node('B')
net.add_nodes([a.name, b.name])
net.show('index.html')