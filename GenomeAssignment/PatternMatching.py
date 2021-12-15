def PatternMatching(Pattern, Genome):
    Position = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i + len(Pattern)] == Pattern:
            Position.append(i)
    return Position


def SymbolToNumbers(Symbol):
    S = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return S[Symbol]


def NumberToSymbols(index):
    S = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    for i in S.keys():
        if S[i] == index:
            return i


def PatternToNumber(Pattern):
    if len(Pattern) == 0:
        return 0
    symbol = Pattern[-1]
    Prefix = Pattern[:-1]
    return 4 * PatternToNumber(Prefix) + SymbolToNumbers(symbol)


def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbols(index)
    Quotient = divmod(index, 4)
    prefixIndex = Quotient[0]
    r = Quotient[1]
    symbol = NumberToSymbols(r)
    PrefixPattern = NumberToPattern(prefixIndex, k - 1)
    return PrefixPattern + symbol


def ComputingFrequencies(Text, k):
    FrequencyArray = []
    for i in range(4 ** k):
        FrequencyArray.append(0)
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i + k]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1
    return FrequencyArray


def FindingFrequentWordsBySorting(Text, k):
    FrequentPatterns = []
    Index = []
    Count = []
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i + k]
        Index.append(PatternToNumber(Pattern))
        Count.append(1)
    SortedIndex = sorted(Index)
    for i in range(len(Text) - k + 1):
        if SortedIndex[i] == SortedIndex[i - 1]:
            Count[i] = Count[i - 1] + 1
    maxCount = max(Count)
    for i in range(len(Text) - k + 1):
        if Count[i] == maxCount:
            Pattern = NumberToPattern(SortedIndex[i], k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns


print(PatternMatching("AAA", "ACTGGTCTTAGGCTACCCAAAGG"))
print(SymbolToNumbers("A"))
print(FindingFrequentWordsBySorting("ACTGGTCTTAGGCTACCCAAAGG", 4))
print(ComputingFrequencies("ACTGGTCTTAGGCTACCCAAAGG",2))
print(NumberToPattern(1, 3))
print(PatternToNumber("AAA"))
print(NumberToSymbols(2))
