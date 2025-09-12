import numpy as np


def is_good(B_, G_, epsilon):
    """
    Returns True if and only if "B_ is epsilon-good in G_".
    """
    n = G_.shape[0]
    little = np.sum(G_[:, B_], 1) < epsilon * len(B_)  # which vertices have little connections with B
    many = np.sum(G_[:, B_], 1) > (1 - epsilon) * len(B_)  # which vertices have many connections with B
    return all(np.logical_or(little, many))  # do all vertices have little or many connections with B?

def witness_is_excellent(A_, B_, G_, epsilon):
    """
    Return True if and only if not "B_ witnesses A_ is not epsilon-excellent in G_".
    """
    n = G_.shape[0]
    many = np.sum(G_[A_, :][:, B_], 1) > (1 - epsilon) * len(B_)  # which vertices of A have many connections with B
    little_many = int(sum(many)) < epsilon * len(A_)  # whether there are little vertices of A with many connections with B
    little = np.sum(G_[A_, :][:, B_], 1) < epsilon * len(B_)  # which vertices of A have little connections with B
    little_little = int(sum(little)) < epsilon * len(A_)  # whether there are little vertices of A with little connections with B
    return little_many or little_little  # whether either of the cases are satisfied

def is_excellent(slices, G_, A_, epsilon, debug=False):
    """
    Returns True if and only if "A_ is epsilon-excellent in G_".
    """
    # First of all, we check whether A is good in G.
    if not is_good(A_, G_, epsilon):
        if debug: print("A is not " + str(epsilon) + "-good.")
        return False
    # For each possible subset B...
    for slice_B in slices:
        # ...if it is good...
        if not is_good(slice_B, G_, epsilon):
            continue
        # ...we check whether it witnesses that A is NOT epsilon-excellent.
        if not witness_is_excellent(A_, slice_B, G_, epsilon):
            if debug: print(" - " + str(slice_B) + " is " + str(epsilon) + "-good...")
            if debug: print("   ...and witnesses A is not " + str(epsilon) + "-excellent.")
            return False
    # If there is NO B witness, A is excellent.
    return True

def _generate_all_slices(current, pos, min_size, n):
    """
    Used in recursion of "generate_all_slices".
    """
    to_return = []
    if pos == n:
        if len(current) < min_size:
            return to_return
        return [current]
    to_return += _generate_all_slices(current + [pos], pos + 1, min_size, n)
    to_return += _generate_all_slices(current, pos + 1, min_size, n)
    return to_return

def generate_all_slices(min_size, start, n):
    """
    Recursive function that generates all possible subsets using vertices from "start" up to "n".
    The subsets need to have at least "min_size" elements.
    """
    current = []
    return _generate_all_slices(current, start, min_size, n)

def generate_all_slices(min_size, start, n):
    """
    Recursive function that generates all possible subsets using vertices from "start" up to "n".
    The subsets need to have at least "min_size" elements.
    """
    current = []
    return _generate_all_slices(current, start, min_size, n)

def _generate_onehots(current, pos, n, min_, max_):
    """
    Used in recursion of "generate_onehots".
    """
    to_return = []
    if pos == n:
        if sum(current) >= min_ and sum(current) <= max_:
            return []
        return [current]
    to_return += _generate_onehots(current + [0], pos + 1, n, min_, max_)
    to_return += _generate_onehots(current + [1], pos + 1, n, min_, max_)
    return to_return

def generate_onehots(n, min_, max_):
    """
    Recursive function that generates all possible lists of {0,1}-valued vectors of length n.
    The lists need to contain less than "min_" or more the "max_" 1's.
    """
    current = []
    return _generate_onehots(current, 0, n, min_, max_)