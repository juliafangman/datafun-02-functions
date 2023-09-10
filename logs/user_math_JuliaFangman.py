print("Julia Fangman")
print('The date is September 1, 2023')
print('I love Tennis')

from logging import Logger
import math
from operator import length_hint
from venv import logger

print(math.sqrt(900))

def area_of_tenniscourt(length, width):
    return length * width
total=area_of_tenniscourt(78,36)
print(total)

logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")

total=area_of_tenniscourt(78,36)
print(total)
total=area_of_tenniscourt(60,20)
print(total)


#three functions that can be used 
# this is about tennis 

#sum function used to calculate the number of grand slam titles won by Federer, Nadal, & Djokovic
federer_grand_slam_titles = 20  
nadal_grand_slam_titles = 22  
djokovic_grand_slam_titles = 23 
grand_slams_counts = (federer_grand_slam_titles, nadal_grand_slam_titles, djokovic_grand_slam_titles)

total_grand_slam_titles = sum(grand_slams_counts)

print("Total Grand Slams won by Federer, Nadal, and Djokovic:", total_grand_slam_titles)

#max function used to calculate the winner with the most grand slam titles 
federer_grand_slam_titles = 20  
nadal_grand_slam_titles = 22 
djokovic_grand_slam_titles = 23

def winners(most_grand_slam_titles):
    federer_grand_slam_titles = 20 
    nadal_grand_slam_titles = 22 
    djokovic_grand_slam_titles = 23 
 
most_grand_slam_titles = max(grand_slams_counts)
if (federer_grand_slam_titles) == most_grand_slam_titles:
    winner = ("Federer")
if (nadal_grand_slam_titles) == most_grand_slam_titles:
    winner = ("Nadal")
if (djokovic_grand_slam_titles) == most_grand_slam_titles:
    winner = ("Djokovic")
print("The winner with the most grand slam titles is", winner)

# min function used to calculate the winner with the most grand slam titles 
federer_grand_slam_titles = 20
nadal_grand_slam_titles = 22
djokovic_grand_slam_titles = 23

least_grand_slam_titles = min(grand_slams_counts)
if (federer_grand_slam_titles) == least_grand_slam_titles:
    player = ("Federer")
if (nadal_grand_slam_titles) == least_grand_slam_titles:
    player = ("Nadal")
if (djokovic_grand_slam_titles) == least_grand_slam_titles:
    player = ("Djokovic")
print("The player with the least grand slam titles is", player)