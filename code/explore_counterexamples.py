from utils import is_good, witness_is_excellent, is_excellent, generate_all_slices, generate_onehots
from pprint import pprint
import numpy as np
import itertools
from tqdm import tqdm


def main():
    """
    Main code that searches for an example of bipartite graph G = U \\union V, such that:
     - U is small_epsilon-good.
     - V is big_epsilon-good.
     - V witnesses that U is not big_epsilon-excellent.
    """
    sizes_U = [i for i in range(5, 9)]
    sizes_V = [i for i in range(5, 9)]
    big_epsilon = 2/5
    small_epsilon = 1/3

    found = False
    for size_U, size_V in itertools.product(sizes_U, sizes_V):  # check for all combinations of sizes
        # setting min and max correctly, we ensure that U can be small-epsilon-good.
        onehots = generate_onehots(size_U, small_epsilon * size_U, (1 - small_epsilon) * size_U)  # neighborhood of each vertex of V with respect to U.

        increasing_sequences = list(itertools.combinations_with_replacement(range(0,len(onehots)), size_V))
        for increasing_sequence in tqdm(increasing_sequences, total=len(increasing_sequences), desc="size_U=" + str(size_U) + "\tsize_V=" + str(size_V)):
            G0 = [[0] * (size_U + size_V)] * size_U + \
             [onehots[ind_] + [0] * size_V for ind_ in increasing_sequence]

            G0 = np.array(G0)
            G_ = G0 + G0.transpose()

            # We make sure that V is big-epsilon-good
            V_ = [i for i in range(size_U, size_U + size_V)]  # vertices of V
            if not is_good(V_, G_, big_epsilon):
                continue

            # make sure V witnesses U is NOT big-epsilon-excellent
            U_ = [i for i in range(size_U)]  # vertices of U
            if witness_is_excellent(U_, V_, G_, big_epsilon):
                continue

            slices = generate_all_slices(1, size_U, size_U + size_V)
            if is_excellent(slices, G_, U_, big_epsilon, debug=False):
                continue
            if not is_excellent(slices, G_, U_, small_epsilon, debug=False):
                continue

            # if we find it, we stop and print it.
            print("FOUND!")
            print("\nU indices: ")
            pprint(U_)
            print("\nV indices:")
            pprint(V_)
            print("\nMatrix of bipartite G = U \\cup V:")
            pprint(G_.tolist())
            print(f"\n - U is {str("{:.2f}".format(small_epsilon))}-good")
            print(f" - V is {str("{:.2f}".format(big_epsilon))}-good")
            print(f" - V witnesses that U is not {str("{:.2f}".format(big_epsilon))}-excellent")
            found = True
            break
        if found:
            break


if __name__ == "__main__":
    main()