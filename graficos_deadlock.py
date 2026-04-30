import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()

#Lista de relacoes
edges =[
      ("R","A"),
      ("A","T"),
      ("X","B"),
      ("B","R"),
      ("B","T"),
      ("W","C"),
      ("S","C"),
      ("C","R"),
      ("C","X"),
      ("T","D"),
      ("W","D"),
      ("T","E"),
      ("E","V"),
      ("E","W"),
      ("U","F"),
      ("F","S"),
      ("V","G"),
      ("G","U")
      ]

#Aadicionando no grafo
G.add_edges_from(edges)

#leyout
pos =nx.spring_layout(G,seed=42)

#Desenho
# Definindo o tamanho da figura (Largura, Altura)
plt.figure(figsize=(10, 8))
 
nx.draw(
    G, pos,
    with_labels=True,
    node_size=2000,
    node_color="skyblue", # Adicionado para melhor visualização
    font_size=10,
    font_weight="bold",
    arrowsize=20 # Ajustado: arrowsize espera um número (pixels), não um Booleano
    )

plt.title("Grafo de dependencias(possivel deadlock")
plt.show()