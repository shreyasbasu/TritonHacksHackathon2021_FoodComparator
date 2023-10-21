# Entrypoint to your webscraping starter kit
import os         # Used to open html page after scraping
import webbrowser
import sys        # Used to end program if error occurs

from convert import avg_price, avg_rating, avg_review
from scraper import scrape_for
from generator import generate


if __name__ == "__main__":

  # Parse user input for queryngs
  print("Welcome to the location comparator app! Please enter your item to compare (e.g. hot dog):\n")
  item = input()
  print("Ah, {}! An excellent choice! Please enter the first of two cities to compare:\n".format(item))
  place1 = input()
  print("Please enter the abrevation of the state: (e.g. ca = california)\n")
  state1 = input()
  print("Second of the two cities:\n")
  place2 = input()
  print("Second abreviated state:\n")
  state2 = input()
  print("Thank you! Generating report...\n\n")

  try:
    # Make the scrapping requests (this may take a few seconds)
    # scrape_for is a function imported from scraper.py
    (prices1, stars1, images1, review1, weather1) = scrape_for(item, place1, state1)
    (prices2, stars2, images2, review2, weather2) = scrape_for(item, place2, state2)

    # calculate the averaged prices and stars of the separate locations
    place1_avg_price = avg_price(prices1)
    place1_avg_rating = avg_rating(stars1)
    place1_avg_review = avg_review(review1)

    place2_avg_price = avg_price(prices2)
    place2_avg_rating = avg_rating(stars2)
    place2_avg_review = avg_review(review2)

  except Exception as e:
    print("Bad input, the program has ended", e)
    sys.exit()

  # Determine the cheaper and higher rated places
  cheaper = place2 if place1_avg_price > place2_avg_price else place1
  higher_rating = place2 if place2_avg_rating > place1_avg_rating else place1

  # Print results and generate html report
  print("In {p1}, the average rating for {it} is {ra} and the average price is {price}"
  .format(p1=place1, it=item, ra=avg_rating(stars1), price=avg_price(prices1)))
  print()
  print("Here are some reviews of the nearby restaurants in {p1}: ".format(p1 = place1))
  print()
  #Print all reviews for place 1
  for i in range(len(place1_avg_review)):
    if i < (len(place1_avg_review) - 1):
      print(place1_avg_review[i])
  print()
  #Weather 1
  print("The current weather in {p1}: ".format(p1 = place1) + weather1)
  print()
  print()
  print("In {p2}, the average rating for {it} is {ra} and the average price is {price}\n"
  .format(p2=place2, it=item, ra=avg_rating(stars2), price=avg_price(prices2)))
  print("Here are some reviews of the nearby restaurants in {p2}: ".format(p2 = place2))
  print()
  #Print all reviews for place 2
  for i in range(len(place2_avg_review)):
    if i < (len(place2_avg_review) - 1):
      print(place2_avg_review[i])
  print()
  #Weather 2
  print("The current weather in {p2}: ".format(p2 = place1) + weather2)
  print()
  print()
  print("Based on this we can conclude that {} is cheaper...".format(cheaper))
  print("and {} is higher rated!".format(higher_rating))

  # Generate the report
  generate(item, [
    {"location":place1, "weather": weather1, "rating":place1_avg_rating, "price":place1_avg_price, "images":images1, },
    {"location":place2, "weather": weather2, "rating":place2_avg_rating, "price":place2_avg_price, "images":images2},
  ])
