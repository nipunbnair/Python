def ReverseCompliment(Text):
    "Generate Reverse Complement of the string"
    RC = ''
    Complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    Text = reversed(Text)
    for i in Text:
        RC = RC + Complement[i]
    return RC


print(ReverseCompliment("ACGTTGCATGTCGCATGATGCATGAGAGCT"))
