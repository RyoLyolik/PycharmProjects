def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    # print(d)
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1
    # print(d)
    for i in range(lenstr1):
        for j in range(lenstr2):
            # print(i,j)
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
               d[(i - 1, j)] + 1,  # deletion
               d[(i, j - 1)] + 1,  # insertion
               d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
               d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition
    return d[lenstr1 - 1, lenstr2 - 1]

print(damerau_levenshtein_distance('казино все', "казино все"))


def detect(s1,s2):
    end = max(len(s1),len(s2)) - min(len(s1),len(s2))
    for i in range(min(len(s1),len(s2))):
        if s1[i] != s2[i]:
            end += 1

    return end

print(detect('казино все', "казино все"))