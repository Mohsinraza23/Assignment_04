import tkinter as tk
from tkinter import simpledialog

class WordGraphComposer:
    def __init__(self, root):
        self.root = root
        self.root.title("Words Graph Composer")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.nodes = []  # List of tuples: (x, y, word)
        self.edges = []
        self.node_radius = 30
        self.selected_node = None

        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        clicked_node = self.get_node_at_position(event.x, event.y)

        if clicked_node:
            if self.selected_node and self.selected_node != clicked_node:
                self.edges.append((self.selected_node, clicked_node))
                self.draw_edge(self.selected_node, clicked_node)
                self.selected_node = None
            else:
                self.selected_node = clicked_node
        else:
            # Ask user for word input
            word = simpledialog.askstring("Input", "Enter a word:")
            if word:
                self.nodes.append((event.x, event.y, word))
                self.draw_node(event.x, event.y, word)

    def get_node_at_position(self, x, y):
        for node in self.nodes:
            dx = node[0] - x
            dy = node[1] - y
            if (dx**2 + dy**2) ** 0.5 <= self.node_radius:
                return node
        return None

    def draw_node(self, x, y, word):
        r = self.node_radius
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="lightgreen", outline="black")
        self.canvas.create_text(x, y, text=word, font=("Arial", 10, "bold"))

    def draw_edge(self, node1, node2):
        self.canvas.create_line(node1[0], node1[1], node2[0], node2[1], width=2, fill="gray")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordGraphComposer(root)
    root.mainloop()