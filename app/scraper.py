import requests
from bs4 import BeautifulSoup
from herbivore_names import herbivores_names_list
from omnivore_names import omnivore_names_list
from carnivore_names import carnivores_names_list
import json

# To get info about dinos of a particular category

url = "https://www.nhm.ac.uk/discover/dino-directory/diet/omnivores/gallery.html"
import json

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
images = []

dino_divs = soup.find_all("li", class_="dinosaurfilter--dinosaur")

for dino in dino_divs:

    images.append(dino.find('img')['src'])


dinos = dict(zip(omnivore_names_list, images))

print(dinos)

with open('omnivores_dictionary.py', 'w') as f:
    f.write(json.dumps(dinos))


# To find dinos of particular category

# url = "https://www.nhm.ac.uk/discover/dino-directory/diet/omnivores/gallery.html"
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")
#
# dino_ps = soup.find_all('p', class_="dinosaurfilter--name dinosaurfilter--name-unhyphenated")
# list1 = []
# for dino in dino_ps:
#     list1.append(dino.text.strip())
#
# with open('omnivore_names.py', 'w') as f:
#     for item in list1:
#         f.write("%s\n" % item)

