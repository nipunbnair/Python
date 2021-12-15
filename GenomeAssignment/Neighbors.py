from Biology.GenomeAssignment.GenomeReplication import hamming_distance
from Biology.GenomeAssignment.PatternMatching import NumberToPattern, PatternToNumber
from Biology.GenomeAssignment.ReverseCompliment import ReverseCompliment


def ImmediateNeighbors(Pattern):
    Neighborhood = [Pattern]
    for i in range(len(Pattern)):
        symbol = Pattern[i]
        for j in ['A', 'C', 'G', 'T']:
            if symbol != j:
                Neighbor = Pattern[0:i] + j + Pattern[i + 1:]
                Neighborhood.append(Neighbor)
    return Neighborhood


def Neighbors(Pattern, d):
    # generate all k-mers of Hamming distance less than d from Pattern.
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return ['A', 'C', 'G', 'T']
    Neighborhood = []
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for i in range(len(SuffixNeighbors)):
        if hamming_distance(Pattern[1:], SuffixNeighbors[i]) < d:
            for j in ['A', 'C', 'G', 'T']:
                Neighborhood.append(j + SuffixNeighbors[i])
        else:
            Neighborhood.append(Pattern[0] + SuffixNeighbors[i])
    return Neighborhood


def IterativeNeighbors(Pattern, d):
    # generate all k-mers of Hamming distance exactly d from Pattern.
    Neighborhood = [Pattern]
    for j in range(d):
        for i in range(len(Neighborhood)):
            Neighborhood.extend(ImmediateNeighbors(Neighborhood[i]))
            Neighborhood = set(Neighborhood)
            Neighborhood = list(Neighborhood)
    return Neighborhood


def FrequentWordsWithMismatchesAndReverseComplements(Text, k, d):
    FrequentPatterns = []
    Neighborhoods = []
    Index = []
    Count = []
    Reverse = []
    for i in range(len(Text) - k + 1):
        Neighborhoods.extend(Neighbors(Text[i:i + k], d))
    for i in range(len(Neighborhoods)):
        Reverse.append(ReverseCompliment(Neighborhoods[i]))
    NeighborhoodArray = Neighborhoods
    NeighborhoodArray.extend(Reverse)
    for i in range(len(Neighborhoods)):
        Pattern = NeighborhoodArray[i]
        Index.append(PatternToNumber(Pattern))
        Count.append(1)
    SortedIndex = sorted(Index)
    for i in range(len(Neighborhoods) - 1):
        if SortedIndex[i] == SortedIndex[i + 1]:
            Count[i + 1] = Count[i] + 1
    maxCount = max(Count)
    print('Max count=', maxCount)
    for i in range(len(Neighborhoods)):
        if Count[i] == maxCount:
            Pattern = NumberToPattern(SortedIndex[i], k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns


def FrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns = []
    Neighborhoods = []
    Index = []
    Count = []
    for i in range(len(Text) - k + 1):
        Neighborhoods.extend(Neighbors(Text[i:i + k], d))
    NeighborhoodArray = Neighborhoods
    for i in range(len(Neighborhoods)):
        Pattern = NeighborhoodArray[i]
        Index.append(PatternToNumber(Pattern))
        Count.append(1)
    SortedIndex = sorted(Index)
    for i in range(len(Neighborhoods) - 1):
        if SortedIndex[i] == SortedIndex[i + 1]:
            Count[i + 1] = Count[i] + 1
    maxCount = max(Count)
    for i in range(len(Neighborhoods)):
        if Count[i] == maxCount:
            Pattern = NumberToPattern(SortedIndex[i], k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns


print(Neighbors("ACTGGTCTTAGGCTACCCAAAGG", 3))
print(ImmediateNeighbors("ACTGGTCTTAGGCTACCCAAAGG"))
print(IterativeNeighbors("ATA", 2))
print(FrequentWordsWithMismatchesAndReverseComplements("TGGTCTTATCTTAGGC", 3, 3))
print(FrequentWordsWithMismatches("TGGTCTTATCTTAGGC", 3, 3))