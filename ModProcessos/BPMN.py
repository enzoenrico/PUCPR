import matplotlib.pyplot as plt

# Criação do gráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Configuração dos nós
nodes = {
    "Academia": (0, 0),
    "Matrícula de Alunos": (1, 1),
    "Agendamento de Aulas": (1, -1),
    "Realização de Aulas": (2, 0),
    "Gerenciamento de Membros": (3, 1),
    "Pagamento": (3, -1),
}

# Configuração das arestas
edges = [
    ("Academia", "Matrícula de Alunos"),
    ("Academia", "Agendamento de Aulas"),
    ("Agendamento de Aulas", "Realização de Aulas"),
    ("Agendamento de Aulas", "Gerenciamento de Membros"),
    ("Realização de Aulas", "Pagamento"),
    ("Gerenciamento de Membros", "Pagamento"),
]

# Desenho dos nós
for node, pos in nodes.items():
    ax.text(pos[0], pos[1], node, ha="center", va="center", bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.3"))
    ax.plot(pos[0], pos[1], "o", color="black")

# Desenho das arestas
for edge in edges:
    start = nodes[edge[0]]
    end = nodes[edge[1]]
    ax.annotate("", xytext=start, xy=end, arrowprops=dict(arrowstyle="->"))

# Configurações estéticas do gráfico
ax.set_xlim(-1, 4)
ax.set_ylim(-2, 2)
ax.axis("off")

# Exibição do gráfico
plt.show()
