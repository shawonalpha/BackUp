from urllib.request import urlopen
url = "https://www.wikipedia.org"

page = urlopen(url) 
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html) 

