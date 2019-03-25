import random

outfile = open('output.txt' , 'w')

#loops 20 times
for i in range(20):
    counter = 0
    R1 = 0
    R2 = 0
    R3 = 0
    R4 = 0
    R5 = 1
    while R1 != R2 or R1 != R3 or R1 != R4 or R1 != R5:
        R1 = random.randint(1,6)
        R2 = random.randint(1,6)
        R3 = random.randint(1,6)
        R4 = random.randint(1,6)
        R5 = random.randint(1,6)
        print("roll: %s %s %s %s %s" % (R1, R2, R3, R4, R5))

    outfile.write('yahtzee in ')
    outfile.write(str(counter))
    outfile.write(' moves\n')

outfile.close()
print('done')