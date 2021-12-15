from Biology.GenomeAssignment.PatternCount import PatternCount


def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = []
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:k + i]
        Count.append(PatternCount(Text, Pattern))
    maxCount = max(Count)
    for i in range(len(Text) - k + 1):
        if Count[i] == maxCount:
            FrequentPatterns.append(Text[i:k + i])
    FrequentPatterns = set(FrequentPatterns)
    return FrequentPatterns


print(FrequentWords("ACTGGTCTTAGGCTACCCAAAGG",3))