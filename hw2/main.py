from math   import log
from string import ascii_lowercase

ABC = ascii_lowercase

def shakespeare_mean_length():
    freqs   = {}
    lengths = { l : 0 for l in ABC }

    with open('shakespeare.txt') as f:
        s = f.read().lower()

        for l in ABC:
            freqs[l] = s.count(l)

        all = sum(freqs.values())

        for l in ABC:
            freqs[l] /= all

        ptree = [(p, [l]) for (l, p) in freqs.items()]

        while len(ptree) > 1:
            ptree.sort()
            new = (ptree[0][0] + ptree[1][0], ptree[0][1] + ptree[1][1])

            for l in new[1]:
                lengths[l] += 1

            ptree = [new] + ptree[2:]

        return sum([freqs[l] * lengths[l] for l in ABC])

print(round(shakespeare_mean_length(), 5))
