import requests
import bs4
from pymongo import MongoClient
import string
from collections import Counter

def pull_lyrics(url):
	text = ''
	r = requests.get(url)
	soup = bs4.BeautifulSoup(r.text)
	body = soup.find_all('div', style="margin-left:10px;margin-right:10px;")
	for p in body:
		text += p.text

	return text.replace('\n', ' ')


def get_urls(url):
	url_list = []
	ra = requests.get(url)
	soupa = bs4.BeautifulSoup(ra.text, "html.parser")
	bodya = soupa.find_all('a', target = "_blank")
	for p in bodya:
		url = 'http://www.azlyrics.com/' + p['href'][2:]
		url_list.append(url)
	return url_list

def remove_brackets(t):
	#removes brackets phrases, as these are usually not lyrics
	to_remove = []
	rem_idx = []
	for i, ch in enumerate(t):
	    if ch == '[':
	        rem = ''
	        for j in range(i, len(t)):
	            rem += t[j]
	            if t[j] == ']':
	                to_remove.append(rem)
	                rem_idx.append((i,j))
	                break

	for p in to_remove:
		t = t.replace(p, " ")
	return t


def get_wordlist(url):
	exclude = set(string.punctuation)

	c = Counter()
	complete_text = ''
	url_list = get_urls(url)
	for url in url_list:
		text = pull_lyrics(url)
		text = remove_brackets(text)
		text = ''.join(ch for ch in text if ch not in exclude).replace('\n', " ").replace(
			'\r', " ").lower()
		complete_text += text
		text_list = text.split(" ")
		c.update(text_list)
	return c, complete_text


if __name__ == '__main__':
	pass