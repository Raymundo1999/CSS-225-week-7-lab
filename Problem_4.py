#Raymundo Sanchez
#Nov16, 2020
#this shows the score of the times to shot in arrow and score
#this also gives you the score you get and arrows that you have left
#meaning it can go until 11 in the list if you get a 0
#this means no points but also you dont lose a arrow
#also if you get a point you lose a arrow this is shows in the "arrows -= 1"
#this shows that you lose a arrow if you get a point
#in the end it will show you your final score and score card
import random

arrows = 10
random_score = 0
score_card = []
while arrows > 0:
    integer = random.randint (0,10)
    score_card.append(integer)
    if integer == 0:
        pass
    elif integer == 10:
        random_score += 20
        arrows -= 1
    else:
        random_score += integer
        arrows -= 1
print ("final Score: ", random_score)
print ("score card", score_card)

