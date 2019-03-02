from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'


#opening connection to page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#Html Parsing
page_soup = soup(page_html, "html.parser")

# Grabs all products and associated information
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, title, shipping\n"

f.write(headers)

# Grab Specific div containing brand "title"
for container in containers:
	brand_container = container.findAll("div", {"class":"item-branding"})
	brand = brand_container[0].a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	title = title_container[0].text

	ship_container = container.findAll("li", {"class":"price-ship"})
	shipping = ship_container[0].text.strip()

	print("brand: " + brand)
	print("title: " + title)
	print("shipping: " + shipping)

	f.write(brand + "," + title.replace(",", "|") + "," + shipping + "\n")




