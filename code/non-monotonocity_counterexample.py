from utils import is_excellent, generate_all_slices
import argparse
from pprint import pprint
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--subset_size", type=int, required=True,
                        help="Size of both sets A and B. This value must be even and \\geq 6. ")
    args = parser.parse_args()

    assert args.subset_size % 2 == 0, f"Given subset_size is not even. "
    assert args.subset_size >= 6, f"Given subset_size is not greater or equal to 6. "

    if args.subset_size > 10:
        print(f"Warning: compute time increases exponentially with subset_size. It is not encouraged to compute values"
              f"higher than 10.")

    r = args.subset_size // 2

    """
    Now we build the matrix B

        |           |           |
        |     0     |     H     |
        |           |           |
    G = |-----------|-----------|
        |           |           |
        |    H^-1   |     0     |
        |           |           |

    where H is

        |           |           |
        |     0     |    1-I    |
        |           |           |
    H = |-----------|-----------|
        |           |           |
        |     J     |     I     |
        |           |           |

    First block (both horizontally and vertically) refers to set A, and second to B
    """

    H_ = [[0] * r + [1 if i != j else 0 for i in range(r)] for j in range(r)] + \
         [[1 if i == r - j - 1 else 0 for i in range(r)] + [1] * r for j in range(r)]
    G0 = [[0] * (2 * r) + line for line in H_] + [[0] * (4 * r)] * (2 * r)
    G_ = np.array(G0) + np.array(G0).transpose()

    A_ = [i for i in range(2 * r)]

    """
    We now test epsilon-excellence of A in G for two values of epsilon: epsilon_1 < epsilon_2.
    We see that despite epsilon_1 being smaller than epsilon_2:
    - A is epsilon_1-excellent.
    - A is NOT epsilon_2-excellent.
    """
    epsilon_1 = 1 / (2 * r - 1)
    epsilon_2 = (r - 1) / (2 * r - 1)

    slices = generate_all_slices(1, 0, 4 * r)  # Generate all subsets

    print(f"Matrix G: ")
    pprint(G_.tolist())
    print(f"A indices: ")
    pprint(A_)

    print("Is A " + str("{:.2f}".format(epsilon_1)) + "-excellent? " + str(
        is_excellent(slices, G_, A_, epsilon_1, debug=False)))
    _ = is_excellent(slices, G_, A_, epsilon_1, debug=True)  # prints some extra info

    print("Is A " + str("{:.2f}".format(epsilon_2)) + "-excellent? " + str(
        is_excellent(slices, G_, A_, epsilon_2, debug=False)))
    _ = is_excellent(slices, G_, A_, epsilon_2, debug=True)  # prints some extra info


if __name__ == '__main__':
    main()