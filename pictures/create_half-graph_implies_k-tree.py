Y_SEP=4
X_SEP=1
X_MATRIX_ADJ = -1
Y_MATRIX_ADJ = 0.7
K=10
CELL_SIZE=0.5
NODE_SIZE=0.3
CAPTION=(f"Example of a $3$-tree in a half-graph with 2 × {K} vertices. \n"
         f"\\emph{{On the left}}, solid lines show adjacent vertices, and dashed lines show non-adjacent vertices. \n"
         f"Pairs of vertices without a line may or may not be connected. \n"
         f"Orange lines and nodes highlight the $3$-tree structure. \n"
         f"\\emph{{On the right}} is the corresponding bi-adjacency matrix. \n"
         f"Again, orange cells highlight edges relative to the $3$-tree structure. ")
FIG_NAME="half-graph_implies_k-tree"
OUTPUT_FILE="pictures/half-graph_implies_k-tree.tex"


def binary_decomposition(value, digits, text=False):
    solution = []
    for _ in range(digits):
        solution.append(int(value % 2))
        value //= 2
    if text:
        return "".join(map(str,reversed(solution)))
    return list(reversed(solution))


def main():
    prefix = f"""\\begin{{figure}}
    \\centering

    \\begin{{tikzpicture}}[
        vertex/.style={{circle, draw, fill=gray!20, minimum size={NODE_SIZE} cm, inner sep=1pt}},
        tree_vertex/.style={{circle, thick, draw=orange!70!red, fill=orange!70!red!20, minimum size={NODE_SIZE} cm, inner sep=1pt}},
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

    # a's
    for i in range(1,K+1):
        vertex_ = "tree_vertex" if i in range(2,10) else "vertex"
        x_coord = X_SEP * i
        y_coord = 0
        nodes += ("\t"
                 + f"\\node[{vertex_}] (a_"
                 + str(i)
                 + r") at ("
                 + str(x_coord)
                 + "," + str(y_coord)
                 + ") {};"
                 + "\n")
    for i in range(8):
        i_ = i + 2
        label = binary_decomposition(i, 3, text=True)
        labels += ("\t" + r"\node[label_a] at (a_"
                   + str(i_)
                   + rf".north) {{$b_{{{label}}}$}};"
                   + "\n")

    # b's
    for i in range(1, K + 1):
        vertex_ = "tree_vertex" if i in range(3,10) else "vertex"
        x_coord = X_SEP * i
        y_coord = - Y_SEP
        nodes += ("\t"
                 + f"\\node[{vertex_}] (b_"
                 + str(i)
                 + r") at ("
                 + str(x_coord)
                 + "," + str(y_coord)
                 + ") {};"
                 + "\n")
    i2label = {
        3: "00",
        4: "0",
        5: "01",
        6: "\\emptyset",
        7: "10",
        8: "1",
        9: "11",
    }
    for i, label in i2label.items():
        labels += ("\t" + r"\node[label_b] at (b_"
                   + str(i)
                   + rf".south) {{$c_{{{label}}}$}};"
                   + "\n")

    # (c,b)
    tree2edge_or_not = {
        (3,2): False, (3,3): True,
        (5,4): False, (5,5): True,
        (7,6): False, (7,7): True,
        (9,8): False, (9,9): True,
        (4,2): False, (4,3): False, (4,4): True, (4,5): True,
        (8,6): False, (8,7): False, (8,8): True, (8,9): True,
        (6,2): False, (6,3): False, (6,4): False, (6,5): False, (6,6): True, (6,7): True, (6,8): True, (6,9): True,
    }
    for i in range(1,K+1):
        for j in range(1,K+1):
            thickness = "thin"
            if (i,j) in tree2edge_or_not:
                continue
            if i < j:
                edges += ("\t"
                          + f"\\draw[dashed edge, {thickness}] (a_{j}) -- (b_{i});\n")
            else:
                edges += ("\t"
                          + f"\\draw[solid edge, {thickness}] (a_{j}) -- (b_{i});\n")
    for i in range(1,K+1):
        for j in range(1,K+1):
            color = "orange!70!red"
            thickness = "thick"
            if (i,j) not in tree2edge_or_not:
                continue
            if tree2edge_or_not[(i,j)]:
                edges += ("\t"
                          + f"\\draw[dashed edge, {thickness}, {color}] (a_{j}) -- (b_{i});\n")
            else:
                edges += ("\t"
                          + f"\\draw[solid edge, {thickness}, {color}] (a_{j}) -- (b_{i});\n")

    # matrix
    matrix_prefix=f"""
\\begin{{scope}}[xshift={2+K*X_SEP} cm]
"""
    matrix_suffix="""   \\end{scope}

"""
    matrix_cells = ""
    matrix_labels = ""
    for i in range(1,K+1):
        if i in range(3,10):
            label = i2label[i]
            matrix_labels += "\t\t" + f"\\node[matrix label] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ}) {{$c_{{{label}}}$}};\n"
        if i in range(2,10):
            label = binary_decomposition(i-2, 3, text=True)
            matrix_labels += "\t\t" + f"\\node[matrix label] at ({X_MATRIX_ADJ-0.1}, {Y_MATRIX_ADJ - i * CELL_SIZE}) {{$b_{{{label}}}$}};\n"

    for i in range(1,K+1):
        for j in range(1,K+1):
            if (i,j) in tree2edge_or_not:
                continue
            else:
                if i > j:
                    matrix_cells += f"\t\t\\node[matrix cell] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{0}};\n"
                else:
                    matrix_cells += f"\t\t\\node[matrix cell, fill=gray!20] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{1}};\n"
    for i in range(1,K+1):
        for j in range(1,K+1):
            if (i,j) in tree2edge_or_not:
                if i > j:
                    matrix_cells += f"\t\t\\node[matrix cell, thick, draw=orange!70!red, text=orange!70!red] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{0}};\n"
                else:
                    matrix_cells += f"\t\t\\node[matrix cell, thick, draw=orange!70!red, fill=orange!70!red!20, text=orange!70!red] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{1}};\n"

    matrix = f"{matrix_prefix}{matrix_cells}{matrix_labels}{matrix_suffix}"

    with open(OUTPUT_FILE, "w") as o_f:
        o_f.write(f"{prefix}{nodes}{edges}{labels}{matrix}{suffix}")


if __name__ == "__main__":
    main()
