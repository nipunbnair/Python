from Bio import SeqIO

for record in SeqIO.parse("Ecolifasta", "fasta"):
    print(record.id)
    print(record.seq.upper())
