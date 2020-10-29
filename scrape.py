import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
hn_text = BeautifulSoup(res.text, 'html.parser')
links = hn_text.select('.storylink')
subtext = hn_text.select('.subtext')

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
	hn = []

	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		score = subtext[idx].select('.score')
		
		if len(score):
			points = int(score[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})

	return sort_stories_by_votes(hn)

pprint.print(create_custom_hn, subtext)