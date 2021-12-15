from Biology.GenomeAssignment.PatternMatching import ComputingFrequencies, NumberToPattern


def ClumpFinding(Genome, k, L, t):
    # We defined a k-mer as a "clump" if it appears many times within a short interval of the genome.
    # More formally, given integers L and t, a k-mer Pattern forms an (L, t)-clump inside a (longer) string Genome
    #  if there is an interval of Genome of length L in which this k-mer appears at least t times.
    FrequentPatterns = []
    Clump = []
    for i in range(4 ** k):
        Clump.append(0)
    for i in range(len(Genome) - L + 1):
        Text = Genome[i:i + L]
        FrequencyArray = ComputingFrequencies(Text, k)
        for index in range(4 ** k):
            if FrequencyArray[index] >= t:
                Clump[index] = 1
    for i in range(4 ** k):
        if Clump[i] == 1:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns


print(ClumpFinding("ACTGGTCTTAGGCTACCCAAAGG", 3, 5, 2))
