import math

n = 4
r = 2
Permutations = math.factorial(n) / math.factorial(n - r)
print(Permutations)
Combinations = Permutations/math.factorial(r)
print(Combinations)

