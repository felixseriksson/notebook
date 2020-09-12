def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator. Handles lists, not sets.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

if __name__ == "__main__":
    for p in powerset([1, 2, 3, 4]):
        print(p)