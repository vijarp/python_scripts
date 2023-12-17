import requests
from bs4 import BeautifulSoup

def get_lichess_rating(username):
  """
  Retrieves the rating of a player from their Lichess username.

  Args:
    username: The Lichess username of the player.

  Returns:
    A string containing the player's rating or None if not found.
  """
  url = f"https://lichess.org/@/{username}"
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser")
  for t in soup.find_all("a",href=lambda x:x and 'perf/bullet' in x):
    try:
      rating = t.find("strong").text
      return rating
    except:
      return "Rating not found"
  # Find the element containing the player's rating
  #rating_element = soup.find("a", class_="inline-rating")

  # Extract and return the rating text if found
  #if rating_element:
  #  return rating_element.text.strip()
  #else:
  #  return None

# Example usage
username = input("Enter username:")
rating = get_lichess_rating(username)

if rating:
  print(f"{username}'s rating is {rating}")
else:
  print(f"Could not find a player with username '{username}'")