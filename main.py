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
    i += 1
    j = 0
    for div_mid_container in div_mid_containers:
        print(div_mid_container)

        a_tag =  div_mid_containers.a
        print("\n\n ITERATION " + str(j) + "\n\n ")

        print(div_mid_container)

        print("\n\n ITERATION " + str(j) + "\n\n ")
        j += 1
        #     a_tag = div_mid_container.findAll("a", {"class": "product-title js-product-url"})
        #     if len(a_tag) == 1:
        #         print("At line i == " + str(i) + " the value is:  " + str(a_tag))
        #     else:
        #         raise ValueError('This a tag should be presented once only.')
        # else:
        #     raise ValueError('This div should be prezented once only.')
