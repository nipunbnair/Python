from Biology.ENDSEM2Project import Genomes
from Biology.ENDSEM2Project.Genomes import Genome1, Genome10, Genome9, Genome8, Genome7, Genome6, Genome5, Genome4, \
    Genome3, Genome2


def countGene(Gene):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count1 = Genome1.count(Gene)
    count2 = Genome2.count(Gene)
    count3 = Genome3.count(Gene)
    count4 = Genome4.count(Gene)
    count5 = Genome5.count(Gene)
    count6 = Genome6.count(Gene)
    count7 = Genome7.count(Gene)
    count8 = Genome8.count(Gene)
    count9 = Genome9.count(Gene)
    count10 = Genome10.count(Gene)
    print(Gene)
    print(count1)
    print(count2)
    print(count3)
    print(count4)
    print(count5)
    print(count6)
    print(count7)
    print(count8)
    print(count9)
    print(count10)


EDAR = 'AAA'
countGene(EDAR)
SLC24A5 = 'GTT'
countGene(SLC24A5)
SLC45A2 = 'ATG'
countGene(SLC45A2)
DARC = 'CAC'
countGene(DARC)
APPBPP2 = 'GCA'
countGene(APPBPP2)
TP1A1 = 'CCA'
countGene(TP1A1)
RTTN = 'AGC'
countGene(RTTN)
KCNMA = 'TTG'
countGene(KCNMA)
MYO5C = 'CGT'
countGene(MYO5C)
