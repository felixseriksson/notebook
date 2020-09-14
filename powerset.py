# def powerset(seq):
#     """
#     Returns all the subsets of this set. This is a generator. Handles lists, not sets.
#     """
#     if len(seq) <= 1:
#         yield seq
#         yield []
#     else:
#         for item in powerset(seq[1:]):
#             yield [seq[0]]+item
#             yield item

# if __name__ == "__main__":
#     for p in powerset([1, 2, 3, 4]):
#         print(p)

from itertools import chain, combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

if __name__ == "__main__":
    for ss in powerset(set([1, 2, 3])):
        print(ss)