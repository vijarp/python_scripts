
from datetime import datetime
list_links = ['www.news.com', 'www.google.com', 'www.yahoo.com', 'www.bbc.com', 'www.msn.com', 'www.facebook.com', 'www.news.google.com']
print(f"Only {len(list_links) * 100 / 120 :.2f}% of the posts contain links")


west = {'date': datetime(2006, 5, 26, 0, 0), 'price': 1432673}

print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")