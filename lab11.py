# Devin Simoneaux
# Week 11 Assignment
# Run a file with scores through the Bowling program that attains scores

from BowlingGame import Game

file = open("testscores.txt","r")

         
for line in file:
    line = line.strip() #take out punctuation
    scoreList = line.split(",") #splits into a list by commas
    scoreList = [int(i) for i in scoreList] #turns list of strings into a list of integers
    finalScore = scoreList.pop() #finalScore is equal to the last value on the list
    g = Game() #reference to BowlingGame.py
    for roll in scoreList: #throws the frames into BowlingGame
        g.roll(roll)
    score = g.score() #gets the score from BowlingGame
    print("Calculated score is {}, and the given score is {}".format(score,  finalScore))
    if score == finalScore: #compares the scores to see if they are right
        print("The score was correct!")
    else:
        print("You were wrong. The score should be", score)
        


        