ProbFire=0.01
ProbSmoke=0.1
ProbSmokebyFire=0.9
ProbFirebySmoke=ProbSmokebyFire*ProbFire/ProbSmoke
print(ProbFirebySmoke)
