'''100 Prisoners'''

from random import randint, sample


# allChainedPathsAreShort :: Int -> IO (0|1)
def allChainedPathsAreShort(n):
    '''1 if none of the index-chasing cycles in a shuffled
       sample of [1..n] cards are longer than half the
       sample size. Otherwise, 0.
    '''
    limit = n // 2
    xs = range(1, 1 + n)
    shuffled = sample(xs, k=n)

    # A cycle of boxes, drawn from a shuffled
    # sample, which includes the given target.
    def cycleIncluding(target):
        boxChain = [target]
        v = shuffled[target - 1]
        while v != target:
            boxChain.append(v)
            v = shuffled[v - 1]
        return boxChain

    # Nothing if the target list is empty, or if the cycle which contains the
    # first target is larger than half the sample size.
    # Otherwise, just a cycle of enchained boxes containing the first target
    # in the list, tupled with the residue of any remaining targets which
    # fall outside that cycle.
    def boxCycle(targets):
        if targets:
            boxChain = cycleIncluding(targets[0])
            return Just((
                difference(targets[1:])(boxChain),
                boxChain
            )) if limit >= len(boxChain) else Nothing()
        else:
            return Nothing()

    # No cycles longer than half of total box count ?
    return int(n == sum(map(len, unfoldr(boxCycle)(xs))))


# randomTrialResult :: RandomIO (0|1) -> Int -> (0|1)
def randomTrialResult(coin):
    '''1 if every one of the prisoners finds their ticket
       in an arbitrary half of the sample. Otherwise 0.
    '''
    return lambda n: int(all(
        coin(x) for x in range(1, 1 + n)
    ))


# MAIN ---
if __name__ == '__main__':
    main()

