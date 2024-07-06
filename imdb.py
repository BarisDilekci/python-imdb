import requests
from bs4 import BeautifulSoup

url = "https://www.sinemalar.com/filmler/en-iyi-filmler"

# Sending a GET request to the URL
response = requests.get(url)

# Getting the content of the response
html_content = response.content

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Finding all movie titles and ratings
movie_titles = soup.find_all("div", {"class": "name"})
movie_ratings = soup.find_all("div", {"class": "right-top-info"})

# Iterating through the movie titles and ratings
for title, rating in zip(movie_titles, movie_ratings):
    # Cleaning and formatting the movie title
    title_text = title.text.strip().replace("\n", "")
    
    # Cleaning and formatting the rating (which represents 'favori' in Turkish)
    rating_text = rating.text.strip().replace("\n", "")
    
    # Printing the formatted output
    print("Movie Title:", title_text)
    print("Rating:", rating_text)
    print("-" * 50)  # Separator for better readability
