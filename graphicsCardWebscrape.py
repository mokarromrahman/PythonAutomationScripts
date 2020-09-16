# using this video as a guide
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import time

PAGE_URL = "https://www.memoryexpress.com/Category/VideoCards?PageSize=120"
uClient = uReq(PAGE_URL)  # this opens the page
page_html = uClient.read()  # reading and saving the html of the page
uClient.close()  # close the client
page_soup = soup(page_html, "html.parser")  # save the html of the page

# filename = "page_html.html"
# f = open(filename, "w")
# f.write(page_soup.tostring())
# f.close()

# find all containers with a graphics card
contianers = page_soup.findAll("div", {"class": "c-shca-icon-item"})
# print(len(contianers)) found 120 items so this is working so far

# for contianer in contianers:
#     print(contianer.)
# save every item we see into a csv element
