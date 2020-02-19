from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.emag.ro/telefoane-mobile/c?ref=search_menu_category'

#opening up connection, grabbing the page

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grab each product
containers = page_soup.findAll("div", {"class":"card-item js-product-data"})
i = 0
# container = containers[0]
# disp = container.findAll("div", {"class":"card-section-mid"})
#
# print(str(disp) + " \n length is " + str(len(disp)))
# lenght = len(containers)

# print("Length is: " + str(lenght))

for container in containers:
    div_mid_containers = container.findAll("div", {"class": "card-section-mid"})
    div_btm_containers = container.findAll("div", {"class": "card-section-btm"})

    i += 1
    for div_mid_container in div_mid_containers:
        a_tag = div_mid_container.find("a", {"class": "product-title js-product-url"})
        print("\n Id : " + str(i) + " element text is: " + a_tag.text.strip())

    for div_btm_container in div_btm_containers:
        a_tag = div_btm_container.find("p", {"class": "product-new-price"})
        print("\n Id : " + str(i) + " element price is: " + a_tag.text.strip())

