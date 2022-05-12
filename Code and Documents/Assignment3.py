p1=1/6 #Probability of 4 appearing on the third toss,
p2=1/6 #Probability of 6 appearing on the first toss,
p3=1/6 #Probability of 5 appearing on the second toss

Pe=p1 # E is the event that 4 appears on the third toss
Pf=p2*p3 # F is the event that 6 and 5 appears respectively on first two tosses
Peuf=Pe*Pf 


Pelf=Peuf/Pf # By formula

print(" The probabilty P(E/F) will be ",Pelf)