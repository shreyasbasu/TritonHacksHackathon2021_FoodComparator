import random
import math
from statistics import mean

"""
PART 5 - Average Price
[list of string prices (e.g. [$, $$]) ] => float
"""
def avg_price(prices):
    
  # Replace the below code to calculate the average prices! 
  # Keep in mind the type of our input (list of string)
  new_price = []
  sum = 0
  for i in range (len(prices)):
    new_price.append(len(prices[i]))
    sum += new_price[i]
  average = sum/len(new_price) # <- TODO Replace this line
  return round(average,2)

"""
PART 5 - Average Rating
[list of numbers] => float
"""
def avg_rating(ratings):

  # Replace the below code to return the average of the values of the input
  # Keep in mind that the input here is a list of numbers
  sum = 0
  for i in range (len(ratings)):
    sum += ratings[i]
  average = sum/len(ratings) # <- TODO Replace this line
  return round(average,2)

def avg_review(review):
  new_review = []
  for i in range(len(review)):
    new_review.append(review[i].getText()[:-6] + "...\"")
  return new_review

"""
Don't change this method
[int, int] => [String, float]
"""
#  Calculates the type of emoji to display for current rating.
def calculate_moons(score, multiplier):
  # 🌑🌘🌓🌖🌕
  MOON_EMOJIS = ["&#x1F311","&#x1F318", "&#x1F317", "&#x1F316", "&#x1F315"]
  score = math.floor(float(score) * multiplier + 0.25) / multiplier
  score_copy = score
  
  display_string = ""
  for i in range (5):
    if(score> 1):
      display_string += MOON_EMOJIS[4]
      score -= 1
    else:
      display_string += MOON_EMOJIS[int(score*4)]
      score = 0

  return (display_string, score_copy)
