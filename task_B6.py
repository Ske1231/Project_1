import requests
from bs4 import BeautifulSoup

url = "https://example.com"
output_file = r"C:\data\web_scrape.txt"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

with open(output_file, "w") as f:
    f.write(soup.prettify())

print(f"✅ Web data saved: {output_file}")
