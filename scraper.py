from bs4 import BeautifulSoup
import requests # Used to request webpages
import urllib   # Used for URL encoding (e.g. La Jolla San Diego CA -> La+Jolla%2C+San+Diego%2C+CA)


# HTTP header we'll use for getting the page
headers = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET',
  'Access-Control-Allow-Headers': 'Content-Type',
}

"""
String, String => ([ratings], [costs])
"""
def scrape_for(query, location, state):
  # Builds the URL for what to scrape
  url = "https://www.yelp.com/search?"
  params = {"find_desc": query, "find_loc": location, "ns": 1}
  url += urllib.parse.urlencode(params)

  url2 = "https://www.wunderground.com/weather/us/"+ state + "/" + location.replace(" ", "-")

  # Scrape the url with BeautifulSoup
  page = requests.get(url, headers)
  scraper = BeautifulSoup(page.content, 'html.parser')

  page2 = requests.get(url2, headers)
  scraper2 = BeautifulSoup(page2.content, 'html.parser')

  # Get all search results
  results = scraper.find_all("div", class_="container__09f24__21w3G")


  """
  PART 3
  hint: refer to results in (line 26)
  """
  # Get all prices
  prices = scraper.find_all("span", class_= "priceRange__09f24__2O6le") # <- TODO Add the span class here

  """
  PART 4
  """
  # Get all star ratings
  stars = scraper.find_all("div", class_="i-stars__09f24__1T6rz") # <- TODO Add the div class here



  """
  New Part (Getting Reviews)
  """
  review = scraper.find_all("p", class_="css-e81eai")
  
  
  """
  New Part (Getting Weather)
  """
  weather = scraper2.find("span", class_="wu-value")
  weather = weather.getText()

  """
  for i in range(len(stars)):
    print(stars[i]["aria-label"][:-12])
    print(type((stars[i]["aria-label"][:-12])))
    stars[i] = float(stars[i]["aria-label"][:-12])
  """
  
  """
  Don't change the methods below
  """
  # Get all images, store only source attributes
  images = scraper.find_all(class_="css-xlzvdl")[:10]
  image_sources = [img["src"] for img in images]

  # turn prices(array of html tags) into numbers
  for i in range(len(prices)):
    prices[i] = prices[i].string

  # turn stars(array of html tags) into numbers as well
  for i in range(len(stars)):
    stars[i] = float(stars[i]["aria-label"][:-12])

  return (prices, stars, image_sources, review, weather)
