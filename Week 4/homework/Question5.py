"""
Function to generate permutations of outcomes
Repetition of outcomes not allowed
"""
import itertools


def gen_permutations(outcomes, length):
    """
    Iterative function that generates set of permutations of outcomes of
    length num_trials. No repeated outcomes allowed
    :param length:
    :param outcomes:
    """

    # ans = {()}

    # for dummy_idx in range(length):
    #     temp = set()
    #
    #     for seq in ans:
    #         for item in outcomes:
    #             new_seq = list(seq)
    #             new_seq.append(item)
    #             temp.add(tuple(new_seq))
    #     ans = temp

    return list(itertools.permutations(outcomes, length))


# Final example for homework problem

outcome = {"a", "b", "c", "d", "e", "f"}

permutations = gen_permutations(outcome, 4)
permutation_list = list(permutations)
permutation_list.sort()
print
print "Answer is", permutation_list[100]
