Y_SEP=4
X_SEP=1
X_MATRIX_ADJ = -1
Y_MATRIX_ADJ = 0.7
K=3
CELL_SIZE=0.5
NODE_SIZE=0.3
CAPTION=(f"Example of the $\epsilon$-excellence property not being monotonic. \n"
         f"\\emph{{On the left}}, a bipartite graph with two independent sets $A$ and $B$. \n"
         f"A simple exhaustive check shows that $A$ is $\\frac{{1}}{{5}}$-excellent. \n"
         f"On the other hand, raising the value of $\epsilon$ up to $\\frac{{2}}{{5}}$ introduces a new \n"
         f"$\\frac{{2}}{{5}}$-good set $B$ witnessing that $A$ is not $\\frac{{2}}{{5}}$-excellent, as half of the "
         f"vertices of $A$ have one truth value, and half the other. \n"
         f"\\emph{{On the right}} is the corresponding bi-adjacency matrix.")
FIG_NAME="non-monotonic_example"
OUTPUT_FILE="pictures/non-monotonic_example.tex"


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

    for i in range(1,2*K+1):
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

    adjacency_matrix = [[0] * K + [1 if i!=j else 0 for i in range(K)] for j in range(K)] + \
        [[1 if i == K-j-1 else 0 for i in range(K)] + [1] * K for j in range(K)]

    for i in range(0,2*K):
        for j in range(0,2*K):
            # if not adjacency_matrix[i][j]:
            #     edges += ("\t"
            #               + f"\\draw[dashed edge] (a_{i+1}) -- (b_{j+1});\n")
            # else:
            if adjacency_matrix[i][j]:
                edges += ("\t"
                          + f"\\draw[solid edge] (a_{i+1}) -- (b_{j+1});\n")

    # matrix
    matrix_prefix=f"""
\\begin{{scope}}[xshift={2+2*K*X_SEP} cm]
"""
    matrix_suffix="""    \\end{scope}

"""
    matrix_cells = ""
    matrix_labels = ""
    Y_ADJUSTMENT = 1
    for i in range(1,2*K+1):
        matrix_labels += "\t\t" + f"\\node[matrix label] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ-Y_ADJUSTMENT}) {{$b_{{{str(i)}}}$}};\n"
        matrix_labels += "\t\t" + f"\\node[matrix label] at ({X_MATRIX_ADJ}, {Y_MATRIX_ADJ - i * CELL_SIZE-Y_ADJUSTMENT}) {{$a_{{{str(i)}}}$}};\n"

    for i in range(0,2*K):
        for j in range(0,2*K):
            if not adjacency_matrix[j][i]:
                matrix_cells += f"\t\t\\node[matrix cell, fill=gray!20] at ({X_MATRIX_ADJ + (i+1) * CELL_SIZE}, {Y_MATRIX_ADJ - (j+1) * CELL_SIZE-Y_ADJUSTMENT}) {{0}};\n"
            else:
                matrix_cells += f"\t\t\\node[matrix cell] at ({X_MATRIX_ADJ + (i+1) * CELL_SIZE}, {Y_MATRIX_ADJ - (j+1) * CELL_SIZE-Y_ADJUSTMENT}) {{1}};\n"

    matrix = f"{matrix_prefix}{matrix_cells}{matrix_labels}{matrix_suffix}"

    A_ = " ".join([f"(a_{i})" for i in range(1,2*K+1)])
    boxes = f"\t\\node[draw, rounded corners, fit={A_}] (box) {{}};\n" + \
            f"\t\\node[left of=box, node distance=3cm] {{$A$}};\n"
    B_ = " ".join([f"(b_{i})" for i in range(1,2*K+1)])
    boxes += f"\t\\node[draw, rounded corners, fit={B_}] (box) {{}};\n" + \
            f"\t\\node[left of=box, node distance=3cm] {{$B$}};\n"

    with open(OUTPUT_FILE, "w") as o_f:
        o_f.write(f"{prefix}{nodes}{boxes}{edges}{labels}{matrix}{suffix}")


if __name__ == "__main__":
    main()
