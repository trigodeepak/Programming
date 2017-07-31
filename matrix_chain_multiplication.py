#Program to find minimum matrix chain multiplication
p = [2,3,6,4,5]
##c = [[0 for i in range(n)]for x in range(m)]
def matrix_chain_order(p):
    n = len(p) - 1 # number of matrices in input
    costs = [[0 for i in range(n)] for j in range(n)] # an empty nxn cost matrix
    # length: number of matrices to consider
    for length in range(2,n+1):
        # start: the 0-index of the start matrix
        for start in range(n-length+1):
            # end: the 0-index of the end matrix
            end = start + length - 1
            costs[start][end] = float('inf')
            # midpoint: the 0-index of the matrix whose right edge is considered
            # the midpoint. Note: this is not the same as the actual index to
            # the right edge (which is midpoint + 1).
            for midpoint in range(start, end):
                possible_cost = costs[start][midpoint] + costs[midpoint+1][end] + p[start] * p[midpoint+1] * p[end+1]
                costs[start][end] = min(costs[start][end], possible_cost)
    for i in costs:
        print i
    return costs[0][n-1]
print matrix_chain_order(p)
