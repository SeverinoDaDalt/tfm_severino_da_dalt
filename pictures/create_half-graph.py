Y_SEP=4
X_SEP=1
K=10
CELL_SIZE=0.5
CAPTION=(f"A half-graph with 2 × {K} vertices. \n"
         f"\emph{{On the left}}, solid lines show adjacent vertices, and dashed lines show non-adjacent vertices. \n"
         f"Pairs of vertices without a line may or may not be connected. \n"
         f"\emph{{On the right}} is the corresponding adjacency matrix.")
FIG_NAME="test_half-graph"
OUTPUT_FILE="pictures/test_half-graph.tex"


def main():
    prefix = f"""\\begin{{figure}}
    \centering

    \\begin{{tikzpicture}}[
        vertex/.style={{circle, draw, fill=gray!20, minimum size=5mm, inner sep=1pt}},
        label_a/.style={{above=2pt, font=\small}},
        label_b/.style={{below=2pt, font=\small}},
        node distance=1.5cm,
        solid edge/.style={{draw, thick, black!60}},
        dashed edge/.style={{draw, dashed, thick, black!40}},
        matrix cell/.style={{draw, minimum size={CELL_SIZE} cm, inner sep=0pt}},
        matrix label/.style={{font=\small, anchor=center}}
    ]
"""
    nodes = ""
    labels = ""
    edges = ""
    suffix = f"""    \end{{tikzpicture}}
    \caption{{{CAPTION}}}
    \label{{fig:{FIG_NAME}}}
\end{{figure}}
"""

    for i in range(K):
        x_coord = X_SEP * i
        # a's
        y_coord = 0
        nodes += ("\t"
                 + r"\node[vertex] (a_"
                 + str(i)
                 + r") at ("
                 + str(x_coord)
                 + "," + str(y_coord)
                 + ") {};"
                 + "\n")
        labels += ("\t" + r"\node[label_a] at (a_"
                   + str(i)
                   + rf".north) {{$a_{str(i)}$}};"
                   + "\n")
        # b's
        y_coord = - Y_SEP
        nodes += ("\t"
                 + r"\node[vertex] (b_"
                 + str(i)
                 + r") at ("
                 + str(x_coord)
                 + "," + str(y_coord)
                 + ") {};"
                 + "\n")
        labels += ("\t" + r"\node[label_b] at (b_"
                   + str(i)
                   + rf".south) {{$b_{str(i)}$}};"
                   + "\n")

    for i in range(K):
        for j in range(K):
            if i < j:
                edges += ("\t"
                          + f"\draw[dashed edge] (a_{i}) -- (b_{j});\n")
            else:
                edges += ("\t"
                          + f"\draw[solid edge] (a_{i}) -- (b_{j});\n")

    with open(OUTPUT_FILE, "w") as o_f:
        o_f.write(f"{prefix}{nodes}{edges}{labels}{suffix}")


if __name__ == "__main__":
    main()
