Y_SEP=4
X_SEP=3
X_MATRIX_ADJ = -1
Y_MATRIX_ADJ = -0.7
K=3
CELL_SIZE=0.5
NODE_SIZE=0.3
CAPTION=(f"\\emph{{On the left}}, an example of a graph, smaller than a $3\\times3$ half-graph, "
         f"for which no induced copies can be found in a $3$-stable graph. "
         f"It is basically a $3\\times3$ half-graph in which $a_1$ and $b_2$ are the same vertex, and an edge is "
         f"added between $a_2$ and $a_3$.\n"
         f"\\emph{{On the right}}, the corresponding adjacency matrix. "
         f"Orange cells highlight edges relative to the $3$-order structure")
FIG_NAME="other_k-order"
OUTPUT_FILE="pictures/other_k-order.tex"


def main():
    prefix = f"""\\begin{{figure}}[h]
    \\centering

    \\begin{{tikzpicture}}[
        vertex/.style={{circle, draw, fill=gray!20, minimum size={NODE_SIZE} cm, inner sep=1pt}},
        label_a/.style={{above=2pt, font=\\small}},
        label_b/.style={{below=2pt, font=\\small}},
        node distance=1.5cm,
        solid edge/.style={{draw, thick, black!60}},
        dashed edge/.style={{draw, dashed, thick, black!40}},
        matrix cell/.style={{draw, minimum size={CELL_SIZE} cm, inner sep=0pt}},
        matrix label/.style={{font=\\small, anchor=center}}
    ]
"""
    nodes = ""
    labels = ""
    edges = ""
    suffix = f"""    \\end{{tikzpicture}}
    \\caption{{{CAPTION}}}
    \\label{{fig:{FIG_NAME}}}
\\end{{figure}}
"""

    for i in range(1,K+1):
        x_coord = X_SEP * i
        # a's
        if i!=1:
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
                       + rf".north) {{$a_{{{str(i)}}}$}};"
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
                   + rf".south) {{$b_{{{str(i)}}}$}};"
                   + "\n")

    for i in range(1,K+1):
        for j in range(1,K+1):
            if i < j:
                # edges += ("\t"
                #           + f"\\draw[dashed edge] (a_{i}) -- (b_{j});\n")
                continue
            else:
                if i == 1:
                    edges += ("\t"
                              + f"\\draw[solid edge] (b_2) to [bend left=20] (b_{j});\n")
                else:
                    edges += ("\t"
                              + f"\\draw[solid edge] (a_{i}) -- (b_{j});\n")
    edges += ("\t"
              + f"\\draw[solid edge] (a_2) to [bend left=20] (a_3);\n")

    M = [[0,1,1,1,0],
        [1,0,1,1,1],
        [1,1,0,1,0],
        [1,1,1,0,0],
        [0,1,0,0,0]]
    colors = [[0, 0, 1, 1, 1],
               [0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0]]
    M_labels = ["a_2", "a_3", "b_1", "b_2", "b_3"]

    # matrix
    matrix_prefix=f"""
\\begin{{scope}}[xshift={2+K*X_SEP} cm]
"""
    matrix_suffix="""    \\end{scope}

"""
    matrix_cells = ""
    matrix_labels = ""
    for i in range(1,6):
        matrix_labels += "\t\t" + f"\\node[matrix label] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ}) {{${{{M_labels[i-1]}}}$}};\n"
        matrix_labels += "\t\t" + f"\\node[matrix label] at ({X_MATRIX_ADJ}, {Y_MATRIX_ADJ - i * CELL_SIZE}) {{${{{M_labels[i-1]}}}$}};\n"

    for i in range(1,6):
        for j in range(1,6):
            if not colors[j-1][i-1]:
                if not M[i-1][j-1]:
                    matrix_cells += f"\t\t\\node[matrix cell, fill=gray!20] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{0}};\n"
                else:
                    matrix_cells += f"\t\t\\node[matrix cell] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{1}};\n"
    for i in range(1,6):
        for j in range(1,6):
            if colors[j-1][i-1]:
                if not M[i-1][j-1]:
                    matrix_cells += f"\t\t\\node[matrix cell, thick, draw=orange!70!red, text=orange!70!red] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{0}};\n"
                else:
                    matrix_cells += f"\t\t\\node[matrix cell, thick, draw=orange!70!red, fill=orange!70!red!20, text=orange!70!red] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{1}};\n"

    matrix = f"{matrix_prefix}{matrix_cells}{matrix_labels}{matrix_suffix}"

    with open(OUTPUT_FILE, "w") as o_f:
        o_f.write(f"{prefix}{nodes}{edges}{labels}{matrix}{suffix}")


if __name__ == "__main__":
    main()
