# -*- coding:utf-8 -*-
from graphviz import Digraph, Graph

# https://graphviz.readthedocs.io/en/stable/manual.html


dot = Digraph(comment="The Round Table")
dot.node('A', "A")
dot.node("B", "B")
dot.node("L", "L")

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

print(dot.source)

dot.format = 'png'
dot.render()

h = Graph('hello', format='svg')
h.edge('Hello', 'World')
print(h.pipe().decode('utf-8'))
