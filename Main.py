import requests
import urllib.request
import sys
import re 

def Main(Quality):
	for a in YTstrams:
		try:
			response = requests.get(f"https://www.youtube.com/oembed?url={a}").json()
			print(f"\n Title   : {response['title']}")
			print(f" Channel : {response['author_name']}")

			vid = re.search(r'https?://www.youtube.com/watch\?v=([A-z0-9-_]*)', a).group(1)
			links = {}
			links["HD"] = (f"https://img.youtube.com/vi/{vid}/maxresdefault.jpg")
			links["SD"] = (f"https://img.youtube.com/vi/{vid}/sddefault.jpg")
			links["HQ"] = (f"https://img.youtube.com/vi/{vid}/hqdefault.jpg")
			links["MQ"] = (f"https://img.youtube.com/vi/{vid}/mqdefault.jpg")

			try:
				image_url = links[f'{Quality}']
				if re.finditer(r'[/\\|":*?]', response['title']):
					title = vid
				else:
					title = response['title']
				filename = (f"{title} ({Quality}).jpg")
				print(" Downloading...")
				resx = int(requests.get(image_url, stream=True).headers['Content-length'])
				urllib.request.urlretrieve(image_url, filename)
				size = resx/1024
				print(f' Successfully Dowloaded ({round(size, 2)} KB) ')
			except Exception as Download_Error:
			    if str(Download_Error) == "HTTP Error 404: Not Found":
			    	print(f" {Quality} Source not Available! Try Using Different Quality...")
			    	print(f" Link : {a}")

			    else:
			    	print(" Error With Video Name! Retrying Using Video ID...")
			    	urllib.request.urlretrieve(image_url, f"{vid}.jpg")
			    	size = resx/1024
			    	print(f' Successfully Dowloaded ({round(size, 2)} KB) ')

		except Exception:
			return (f"\n Video Link Does not Exist : {a} \n")

if __name__ == "__main__":
	YTstrams = []
	while True:
		_link = input("\n YouTube Link : ")
		if len(_link) == 0:
			break 
		else:
			if re.match(r'https://www.youtube.com/watch\?v=[A-z0-9-_]*', _link):
				YTstrams.append(_link)
				continue
			else:
				print(f" Invalid YouTube Link : {_link}")
				continue
	QY = input("\n Quality ( HD SD HQ MQ ) : ").upper()
	if len(QY) == 2:
		if QY == str("HD") or str("SD") or str("HQ") or str("MQ"):
			Main(QY)
		else:
			print(" Invalid Quality :/")
			sys.exit()
	else:
		print(" Invalid Quality :/")
		sys.exit()
