import requests
import urllib.request
import sys
import re 

def Main(Quality):
	for a in list(set(YTstrams)):
		try:
			response = requests.get(f"https://www.youtube.com/oembed?url={a}").json()
			print("\n$ Title   : %s" % response['title'])
			print("$ Channel : %s" % response['author_name'])
			vid = re.search(r'v=(.+)', a).group(1)
			links = {}
			links["HD"] = ("https://img.youtube.com/vi/%s/maxresdefault.jpg" % vid)
			links["SD"] = ("https://img.youtube.com/vi/%s/sddefault.jpg" % vid)
			links["HQ"] = ("https://img.youtube.com/vi/%s/hqdefault.jpg" % vid)
			links["MQ"] = ("https://img.youtube.com/vi/%s/mqdefault.jpg" % vid)
			try:
				image_url = links[Quality]
				strlst = r'/\:*?"<>|'
				for item in strlst:
					response['title'] = response['title'].replace(item, '')
				filename = ("%s (%s).jpg" % (response['title'], Quality))
				print("$ Downloading... (%s)" % Quality)
				resx = int(requests.get(image_url, stream=True).headers['Content-length'])
				urllib.request.urlretrieve(image_url, filename)
				size = resx/1024
				print("$ Successfully Dowloaded (%i KB)" % round(size, 2))
			except Exception as Download_Error:
			    if str(Download_Error) == "HTTP Error 404: Not Found":
			    	print("$ %s Source not available Downloading in HQ..." % Quality)
			    	filename = ("%s (%s).jpg" % (response['title'], 'HQ'))
			    	resx = int(requests.get(links['HQ'], stream=True).headers['Content-length'])
			    	print("$ Downloading... (%s)" % 'HQ')
			    	urllib.request.urlretrieve(links['HQ'], filename)
			    	size = resx/1024
			    	print("$ Successfully Dowloaded (%i KB)" % round(size, 2))
			    	pass
		except Exception:
			print("\n$ Video Link Does not Exist : %s" % a)
			pass

if __name__ == "__main__":
	YTstrams = []
	while True:
		_link = input("\n$ YouTube Link : ")
		if len(_link) == 0:
			break 
		else:
			if re.match(r'^https?://w{3}\.youtube\.com/watch\?v=(.+)$', _link):
				YTstrams.append(_link)
				continue
			else:
				continue
	QY = input("\n Quality ( HD SD HQ MQ ) : ").upper()
	if len(QY) == 2:
		if QY == str("HD") or str("SD") or str("HQ") or str("MQ"):
			Main(QY)
		else:
			sys.exit()
	else:
		sys.exit()
