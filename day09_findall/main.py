from bs4 import BeautifulSoup
import requests

# site = "https://httpbun.com"
site = "https://www.bbc.com/news"

def getRequest(site):
	try:
		content = requests.get(site, timeout=5)
	except requests.exceptions.RequestException as e:
		print(f"Request failed: {e}")
		return None
	
	if content.status_code != 200:
		print(f"Non-200 status code: {content.status_code}")
		return None
	
	soup = BeautifulSoup(content.text, "html.parser")
	return soup if soup is not None else "No content to parse"

def getPageTitle(soup):
	title_tag = soup.title
	
	if not title_tag or not title_tag.string:
		return "No title found"

	return title_tag.string.strip() 

def findAll(soup, tag):
	elements = soup.find_all(tag)
	results = []
	
	for el in elements:
		text = el.get_text(strip=True)
		if text:
			results.append(text)	
	
	return results


soup = getRequest(site)
pageTitle = getPageTitle(soup)
print(pageTitle)
headlines = findAll(soup, "h2")

for headline in headlines:
	print(headline)