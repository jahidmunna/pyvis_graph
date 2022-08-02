from turtle import color
from pyvis.network import Network

net = Network(directed=True)
net.add_node("Start", label="Start", shape="ellipse", color="green")
net.add_node("Throttling", label="Throttling", shape="box")   

net.add_edge("Start", "Throttling")

net.show("sample_graph.html")
