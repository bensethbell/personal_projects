import requests
import bs4
from pymongo import MongoClient
import string
from collections import Counter

def pull_lyrics(url, website = 'ohhla'):
	text = ''
	r = requests.get(url)
	soup = bs4.BeautifulSoup(r.text)
	if website == 'rapgenius':
		body = soup.find_all('div', class_ = 'lyrics')
	elif website == 'ohhla':
		body = soup.find_all('div', style="float: left; min-width: 560px;")
	else:
		body = soup.find_all('div', style="margin-left:10px;margin-right:10px;")
	for p in body:
		text += p.text

	return text#.replace('\n', ' ')

def text_to_dict_ohhla(text, dic = {}):
	dic_artist = {}
	dic_albums = {}
	dic_songs = {}

	dic[artist] = 'Error'
	dic[albums] = {}
	dic[albums][1][song] = 'Error'
	dic[albums][1][song]
	album = 'Error'
	song = 'Error'
	for line in text.split()


def get_urls(url):
	url_list = []
	ra = requests.get(url)
	soupa = bs4.BeautifulSoup(ra.text, "html.parser")
	bodya = soupa.find_all('a', target = "_blank")
	for p in bodya:
		url = 'http://www.azlyrics.com/' + p['href'][2:]
		url_list.append(url)
	return url_list

def get_urls_ohhla(artist_url):
	urls = []
	url = artist_url
	stem = "/".join(url.split('/')[:-1])
	r_url = requests.get(url)
	soup_url = bs4.BeautifulSoup(r_url.text)
	for url in soup_url.find_all('a'):
		urls.append(stem + '/' + url['href'])
	return urls

# def get_album_urls_ohhla(album_url)

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