import requests
from bs4 import BeautifulSoup
import certifi

url = "https://www.google.com"

try:
	response = requests.get(url, timeout=10, verify=certifi.where())
	status = response.status_code
	print(status)
except requests.exceptions.SSLError as error:
	print(f"SSL verification failed: {error}")
	print("Try updating certificates: pip install --upgrade certifi")



#exo1
import requests
from bs4 import BeautifulSoup
import json

url = "http://www.bu.edu/president/boston-university-facts-stats/"

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data — the page organizes facts in <h3> and <ul>/<p>
data = {}

# Example extraction approach: collect sections with headers
for section in soup.find_all(['h2', 'h3']):
    title = section.get_text(strip=True)
    content = []

    # Collect following siblings until next header
    for sibling in section.find_next_siblings():
        if sibling.name in ['h2', 'h3']:
            break
        
        # Lists of facts
        if sibling.name == 'ul':
            for li in sibling.find_all('li'):
                content.append(li.get_text(strip=True))

        # Paragraphs
        elif sibling.name == 'p':
            content.append(sibling.get_text(strip=True))

    if content:
        data[title] = content

# Save output as JSON
with open("bu_facts.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(" Data scraped and saved to bu_facts.json")




import requests
from bs4 import BeautifulSoup
import certifi
url = "https://www.google.com"
response = requests.get(url)
content = response.content 
soup = BeautifulSoup(content, "html.parser")
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)
tables = soup.find_all("table",{ "cellpadding": "3"})
table = tables[0]
for td in table.find('tr').find_all('td'):
	print(td.text)