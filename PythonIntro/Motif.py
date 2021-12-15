from Bio.Seq import Seq
from Bio import SeqUtils

sequence = Seq("AGCGATCTAGCATACTTATACGCGCGCAGCTATCGATCACTTGTGCTAGTAAAGTGCGCGCCGCATTAAAGTGCTAGCTAGCTACTTAGCTAGCTAGTCG")
pattern = Seq("ACTT")
results = SeqUtils.nt_search(str(sequence), pattern)
size = len(results)
print("Number of occurences: ", (size - 1))
print(results)