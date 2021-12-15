def hamming_distance(string1, string2):
    distance = 0
    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance


example_dist = hamming_distance("ACTTCA", "ACTTGA")
print(example_dist)
