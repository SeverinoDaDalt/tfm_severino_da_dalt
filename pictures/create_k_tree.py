K=3
Y_SEP=1.8
Y_EXP=0.9
X_SEP=2.2
CELL_SIZE=0.3
CAPTION=(f"Example of a {K}-tree. \n"
         f"Notice that connections between disjoint sub-trees are not defined, and may be edges or non-edges in \n"
         f"any combination.")
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
        vertex/.style={{circle, draw, fill=gray!20, minimum size={CELL_SIZE}cm, inner sep=1pt}},
        label/.style={{below=2pt, font=\\small}},
        solid edge/.style={{draw, thick, black!60}},
        dashed edge/.style={{draw, dashed, thick, black!40}},
    ]
"""
    nodes = ""
    branches = ""
    labels = ""
    edges = ""
    suffix = f"""    \\end{{tikzpicture}}
    \\caption{{{CAPTION}}}
    \\label{{fig:{FIG_NAME}}}
\\end{{figure}}
"""

    for i in range(K+1):
        for j in range(2**i):
            x_coord = (j+.5) * 2**(K-i) * X_SEP
            y_coord = (Y_SEP * i) * Y_EXP**i
            sub_ = binary_decomposition(j,i,text=True)
            nodes += ("\t"
                     + r"\node[vertex] (a_"
                     + sub_
                     + r") at ("
                     + str(x_coord)
                     + "," + str(y_coord)
                     + ") {};"
                     + "\n")
            labels += ("\t" + r"\node[label] at (a_"
                       + sub_
                       + rf".south) {{$a_{{{sub_ if sub_ else emptyset}}}$}};"
                       + "\n")

    for i in range(K):
        for j in range(2**i):
            prec = binary_decomposition(j,i,text=True)
            node = f"a_{prec}"
            for k in range(2**(K-i)):
                cont = binary_decomposition(k,K-i,text=True)
                branch = f"a_{prec}{cont}"
                if cont[0] == "0":
                    edges += ("\t"
                              + f"\\draw[dashed edge] ({node}) -- ({branch});\n")
                else:
                    edges += ("\t"
                              + f"\\draw[solid edge] ({node}) -- ({branch});\n")


    with open(OUTPUT_FILE, "w") as o_f:
        o_f.write(f"{prefix}{nodes}{edges}{labels}{suffix}")

if __name__ == "__main__":
    main()
