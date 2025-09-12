K=3
Y_SEP=1.4
Y_EXP=0.9
X_SEP=1.4
CELL_SIZE=0.5
NODE_SIZE=0.3
X_MATRIX_ADJ = -1
Y_MATRIX_ADJ = 3.7
CAPTION=(f"\\emph{{On the left}}, example of a {K}-tree. \n"
         f"Solid lines show adjacent vertices, and dashed lines show non-adjacent vertices. \n"
         f"Pairs of vertices without a line may or may not be connected. \n"
         f"In particular, notice that connections between disjoint sub-trees are not defined, and may be edges or non-edges in \n"
         f"any combination (e.g. the pair $(c_1, c_{{01}})$). \n"
         f"\\emph{{On the right}}, the corresponding bi-adjacency matrix. ")
FIG_NAME="k_tree"
OUTPUT_FILE="pictures/k-tree.tex"

emptyset = r"\emptyset"

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
        vertex/.style={{circle, draw, fill=gray!20, minimum size={NODE_SIZE}cm, inner sep=1pt}},
        label_c/.style={{below=2pt, font=\\small}},
        label_b/.style={{above=2pt, font=\\small}},
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

    for i in range(K+1):
        for j in range(2**i):
            direction = "north" if i == K else "south"
            letter = "b" if i == K else "c"
            x_coord = (j+.5) * 2**(K-i) * X_SEP
            y_coord = (Y_SEP * i) * Y_EXP**i
            sub_ = binary_decomposition(j,i,text=True)
            nodes += ("\t"
                     + f"\\node[vertex] ({letter}_"
                     + sub_
                     + r") at ("
                     + str(x_coord)
                     + "," + str(y_coord)
                     + ") {};"
                     + "\n")
            labels += ("\t" + f"\\node[label_{letter}] at ({letter}_"
                       + sub_
                       + rf".{direction}) {{${letter}_{{{sub_ if sub_ else emptyset}}}$}};"
                       + "\n")

    connections = {}
    for i in range(K):
        for j in range(2**i):
            prec = binary_decomposition(j,i,text=True)
            node = f"c_{prec}"
            for k in range(2**(K-i)):
                cont = binary_decomposition(k,K-i,text=True)
                branch = f"b_{prec}{cont}"
                if cont[0] == "0":
                    edges += ("\t"
                              + f"\\draw[dashed edge] ({node}) -- ({branch});\n")
                    connections[(node,branch)] = False
                else:
                    edges += ("\t"
                              + f"\\draw[solid edge] ({node}) -- ({branch});\n")
                    connections[(node,branch)] = True

    # matrix
    matrix_prefix=f"""
\\begin{{scope}}[xshift={2+2**K*X_SEP} cm]
"""
    matrix_suffix="""    \\end{scope}

"""
    matrix_cells = ""
    matrix_labels = ""
    i2sub = ["00", "0", "01", emptyset, "10", "1", "11"]
    for i in range(1,2**K+1):
        sub_ = binary_decomposition(i-1,K,text=True)
        matrix_labels += "\t\t" + f"\\node[matrix label] at ({X_MATRIX_ADJ-0.1}, {Y_MATRIX_ADJ - i * CELL_SIZE}) {{$b_{{{sub_}}}$}};\n"
    for i in range(1, 2 ** K):
        matrix_labels += "\t\t" + f"\\node[matrix label] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ}) {{$c_{{{i2sub[i-1]}}}$}};\n"

    for i in range(1,2**K):
        node = f"c_{i2sub[i-1] if i2sub[i-1] != emptyset else ""}"
        for j in range(1,2**K+1):
            branch = f"b_{binary_decomposition(j-1,K,text=True)}"
            if (node,branch) in connections and connections[(node,branch)]:
                matrix_cells += f"\t\t\\node[matrix cell] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{1}};\n"
            elif (node,branch) in connections and not connections[(node,branch)]:
                matrix_cells += f"\t\t\\node[matrix cell, fill=gray!20] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{0}};\n"
            else:
                matrix_cells += f"\t\t\\node[matrix cell, fill=gray!8] at ({X_MATRIX_ADJ + i * CELL_SIZE}, {Y_MATRIX_ADJ - j * CELL_SIZE}) {{-}};\n"

    matrix = f"{matrix_prefix}{matrix_cells}{matrix_labels}{matrix_suffix}"

    with open(OUTPUT_FILE, "w") as o_f:
        o_f.write(f"{prefix}{nodes}{edges}{nodes}{labels}{matrix}{suffix}")  # nodes are repeated to avoid edges on top of nodes
                                                                             # (and they need to be defined to draw edges)

if __name__ == "__main__":
    main()
