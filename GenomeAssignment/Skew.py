def Skew(Genome):
    set = {'C': -1, 'G': 1, 'A': 0, 'T': 0}
    skew = [0]
    for i in range(len(Genome)):
        skew.append(skew[i] + set[Genome[i]])
    return skew


def MinimumSkew(Genome):
    # Find a position in a genome where the skew diagram attains a minimum
    skew = Skew(Genome)
    Mines = []
    Mines = min(skew)
    #print(Mines)
    #for i in range(len(skew)):
     #   if skew[i] == Mines:
       #     Mines.append(skew[i])
    return Mines


print(Skew("ACTGGTCTTAGGCTACCCAAAGG"))
print(MinimumSkew("ACTGGTCTTAGGCTACCCAAAGG"))
