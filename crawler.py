# Importing Required Libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

# Reading the first URL
read_url = urlopen("https://en.wikipedia.org/wiki/Tom_Cruise")
bsobj = soup(read_url.read())

# Creating a list to store all the links
initial_list = []
for link in bsobj.find("div", {"id": "bodyContent"}).find_all('a', href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        initial_list.append(link.attrs['href'])
print(len(initial_list))

# Showing some links
for i in range(10):
    print(initial_list[i])


# Defining a function which generates the correct URL
def generate_url(link):
    return "https://en.wikipedia.org" + link


for idx in range(50):
    readLink = generate_url(initial_list[idx])
    try:
        read_url = urlopen(readLink)
        bsobj = soup(read_url.read())

        # Creating a dict to store links temporarily
        temp_list = []
        for innerLink in bsobj.find("div", {"id": "bodyContent"}).find_all('a', href=re.compile("^(/wiki/)((?!:).)*$")):
            if 'href' in innerLink.attrs:
                temp_list.append(innerLink.attrs['href'])
                df = pd.DataFrame(temp_list)
                df.to_csv("tom" + initial_list[idx].replace("/", "_") + ".csv")
            print(f"{idx}. Completed - {initial_list[idx]}")

    except:
        break