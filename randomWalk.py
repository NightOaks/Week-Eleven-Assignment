# Devin Simoneaux
# Week 11 Assignment
#CIS-125
# Basic Structure for a Random Walk simulation
'''

You flip a coin.
If it comes up heads, you take a step forward;
tails means to take a step backward.
Repeat this n times.
Calculate distance from start

Repeat this process a large number of times.
Calculate and print the average for a given value of n
Start with 100 to 1000, step 10
'''

import random

# Define ranges here

startRange = 100
endRange = 1000 
stepCount = 10

def main():
    printHeader()
    for n in range(startRange,endRange,stepCount):
        averageDistance = getRandomWalk(n)
        print("For {} steps, the average distance is: {}".format(n,averageDistance))


def printHeader():
    print("You flip a coin. If it comes up heads, you take a step forward; tails means to take a step backward. Repeat this n times. Calculate distance from start")

def getRandomWalk(steps):
    avgDistance = 0
    for i in range(steps):
        direction = random.randint(0,1) # Calculate a random walk of given steps
        if direction == 0: 
            avgDistance -= 1 #take a step back
        elif direction == 1:
            avgDistance += 1 #take a step forward
        
    return avgDistance # replace with actual average

if __name__ == "__main__":
    main()