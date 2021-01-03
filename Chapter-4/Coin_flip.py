import random
numberOfStreaks = 0
x='H'
y='T'
for experimentNumber in range(10000):
    toss=[]
    streak=0
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        if random.randint(0,1)==0:
            toss.append(x)
        else:
            toss.append(y)
    # Code that checks if there is a streak of 6 heads or tails in a row
    for c in range(99):
        if toss[c]==toss[c+1]:
            streak+=1
        else:
            if streak==6: numberOfStreaks+=1
            streak=0
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
