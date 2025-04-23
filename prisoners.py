# 100 Prisoners

from random import randint, sample

# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Two sampling techniques constrasted with 100 drawers
       and 100 prisoners, over 100,000 trial runs.
    '''
    halfOfDrawers = randomRInt(0)(1)

    def optimalDrawerSampling(x):
        return allChainedPathsAreShort(x)

    def randomDrawerSampling(x):
        return randomTrialResult(halfOfDrawers)(x)

    # kSamplesWithNBoxes :: Int -> Int -> String
    def kSamplesWithNBoxes(k):
        tests = range(1, 1 + k)
        return lambda n: '\n\n' + fTable(
            str(k) + ' tests of optimal vs random drawer-sampling ' +
            'with ' + str(n) + ' boxes: \n'
        )(fName)(lambda r: '{:.2%}'.format(r))(
            lambda f: sum(f(n) for x in tests) / k
        )([
            optimalDrawerSampling,
            randomDrawerSampling,
        ])

    print(kSamplesWithNBoxes(10000)(10))

    print(kSamplesWithNBoxes(10000)(100))

    print(kSamplesWithNBoxes(100000)(100))