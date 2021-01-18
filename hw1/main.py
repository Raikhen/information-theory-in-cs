from math   import log
from string import ascii_lowercase

abc = ascii_lowercase

def entropy(distr):
    op = lambda p: - p * log(p, 2) if p != 0 else 0
    return round(sum([op(p) for p in distr]), 3)

def entropy_from_table():
    with open('english_freq.dat') as f:
        vals    = [int(line.split()[1]) for line in f]
        distr   = [val / sum(vals) for val in vals]

        return entropy(distr)

def shakespeare_entropy():
    occurrences = {}

    for l in abc:
        occurrences[l] = 0

    with open('shakespeare.txt') as f:
        s = f.read().lower()

        for l in s:
            if l in abc:
                occurrences[l] += 1

        vals    = occurrences.values()
        distr   = [val / sum(vals) for val in vals]

        return entropy(distr)

def next_letter():
    pairs = {}

    for first in abc:
        pairs[first] = {}

        for second in abc:
            pairs[first][second] = 0

    with open('shakespeare.txt') as f:
        s = f.read().lower()

    for i, l in enumerate(s[:-1]):
        if l in abc:
            if s[i + 1] in abc:
                pairs[l][s[i + 1]] += 1

    flipped = {}

    for second in abc:
        flipped[second] = {}

        for first in abc:
            flipped[second][first] = pairs[first][second]

    # Computing H(X)
    vals        = [sum(pairs[l].values()) for l in abc]
    distr       = [val / sum(vals) for val in vals]
    x_entropy   = entropy(distr)

    # Computing H(Y)
    vals        = [sum(flipped[l].values()) for l in abc]
    distr       = [val / sum(vals) for val in vals]
    y_entropy   = entropy(distr)

    # Computing H(Y|X)
    cond_h  = {}
    p_x     = {}
    total   = sum([sum(pairs[l].values()) for l in abc])

    for l in abc:
        p_x[l]      = sum(pairs[l].values()) / total
        vals        = pairs[l].values()
        distr       = [val / sum(vals) for val in vals]
        cond_h[l]   = entropy(distr)
        print(f'{l} & $\\h(Y | X = {l}) = {cond_h[l]}$ \\\\')

    y_x_entropy = sum([p_x[l] * cond_h[l] for l in abc])

    # Mutual information
    info = y_entropy - y_x_entropy

    return (x_entropy, y_entropy, y_x_entropy, info)

print(entropy_from_table())
print(shakespeare_entropy())
print(next_letter())
