from Biology.GenomeAssignment.GenomeReplication import hamming_distance


def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count += 1
    return count


def ApproximatePatternCount(Text, Pattern, d):
    "count pattern in the text"
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if hamming_distance(Text[i:i + len(Pattern)], Pattern) <= d:
            count += 1
    return count


def PatternPosition(Genome, Pattern, d):
    Position = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if hamming_distance(Genome[i:i + len(Pattern)], Pattern) <= d:
            Position.append(i)
    return Position


print(PatternCount("ACTGGTCTTAGGCTACCCAAAGG", "AAG"))
print(PatternPosition("ACTGGTCTTAGGCTACCCAAAGG", "AAG",2))