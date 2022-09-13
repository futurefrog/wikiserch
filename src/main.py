import networkx as nx
from pyvis.network import Network
import requests
from bs4 import BeautifulSoup

BLACKLIST = ['Википедия:Руководство для быстрого старта']
URL = 'https://ru.wikipedia.org'

class Node:
    def __init__(self, url, deep, parent= None, name=None):
        
        self.url = url
        self.name = name if name else self.url.split('/')[-1]
        self.child = []
        self.deep = deep
        self.parent = parent

    def get_child(self):
        if not self.child:
            r = requests.get(self.url).text
            soup = BeautifulSoup(r, 'html.parser')
            for x in soup.select('p > a[title]'):
                self.child.append(Node(url = URL + x['href'], name = x['title'], deep= self.deep + 1, parent=self.name))
            return self.child
        else:
            return self.child
    

class Tree:
    def __init__(self, deep_max = float('inf')):
        self.deep_max = deep_max
        self.nodes = []
        self.net = Network(width = 1920, height=1080)

    def create_main_node(self, url, name=None):
        self.mnode = Node(url=url, deep=0, name=name)
        self.nodes.append(self.mnode)
    

    def collect_tree(self):
        stack = self.mnode.get_child()
        self.nodes += stack
        while len(stack) != 0:
            nnode = stack.pop()
            #print(nnode.name)
            if nnode.deep < self.deep_max:
                stack += [x for x in nnode.get_child() if not(self.check_in_stack(nodes=self.nodes, node=x))]
            #print(len(self.nodes))

    def check_in_stack(self, nodes, node):
        nnode = node.name
        if nnode not in BLACKLIST:
            for x in nodes:
                if x.name == nnode:
                    return True
            self.nodes.append(node)
            return False
        else:
            return True
    
    def graph_visualization(self):
        for node in self.nodes:
            print(node.name)
            self.net.add_node(node.name)
            if node.parent:
                self.net.add_edge(node.name, node.parent)
        self.net.show_buttons(filter_=['physics'])
        self.net.show('index2.html')

if __name__ == '__main__':
    try:
        tree = Tree(deep_max=2)
        tree.create_main_node(url='https://ru.wikipedia.org/wiki/Атом')
        tree.collect_tree()
        tree.graph_visualization()
    except:
        tree.graph_visualization()
