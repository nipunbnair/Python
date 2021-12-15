from Biology.GenomeAssignment.GenomeReplication import hamming_distance
kmer = 4
in_genome = "ACGTTGCATGTCGCATGATGCATGAGAGCT";
in_mistake = 1;
out_result = [];
mismatch_list = []

for i in range(len(in_genome) - kmer + 1):
    v = in_genome[i:i + kmer]
    out_result.append(v)
for i in range(len(out_result)):
    for j in range(i + 1, len(out_result)):
        if hamming_distance(out_result[i], out_result[j]) <= in_mistake:
            mismatch_list.append(out_result[j])
    print(mismatch_list)
