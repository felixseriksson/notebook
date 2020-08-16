# Used to query max value on an interval over an unsorted list.
# For sorted lists, binary search is often more efficient

def build(arr):
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = arr[i]

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1) :
        tree[i] = max(tree[i << 1], tree[i << 1 | 1])

# function to get """max""" on interval [l, r)
def query(l, r) :
    res = 0

    # loop to find the sum in the range
    l += n
    r += n

    while l < r:

        if (l & 1):
            res = max(res, tree[l])
            l += 1

        if (r & 1):
            r -= 1
            res = max(res, tree[r])

        l >>= 1
        r >>= 1

    return res