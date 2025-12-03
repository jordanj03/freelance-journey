from bs4 import BeautifulSoup
import requests

def getPageTitle(site):
	try:
		content = requests.get(site, timeout=5)
	except requests.exceptions.RequestException as e:
		print(f"Request failed: {e}")
		return None

	if content.status_code != 200:
		print(f"Non-200 status code: {content.status_code}")
		return None
	content = content.text
	
	s = BeautifulSoup(content, "html.parser")
	title_tag = s.title.text

	return title_tag.strip() if title_tag != None else "No title found"

pageTitle = getPageTitle("https://httpbun.com")
print(pageTitle)