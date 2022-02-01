from pythonp2p import node
import pytest
import time
import random

totalnodes = 10
nodes = [] 

for n in range(totalnodes):
    port = random.randint(1000,9999)
    nodes[n].append(node.Node(port, port+1))

    if n > 0:
        nodes[n].connect_to("127.0.0.1", node[n-1].port)
