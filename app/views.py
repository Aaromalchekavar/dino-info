from django.shortcuts import render
from bs4 import BeautifulSoup
from sys import getsizeof
from .dinonames import dinos
from app.herbivores_dictionary import herbs
from app.carnivores_dictionary import carns
from app.omnivores_dictionary import omnis
import requests
import random

# Create your views here.

def index(request):
    info = {}
    name = None
    img_link = None

    if request.GET.get('name'):
        name = request.GET.get('name')
        print(name)
        list1 = []
        list2 = []
        page_link = "https://www.nhm.ac.uk/discover/dino-directory/" + name.lower() + ".html"

        page = requests.get(page_link)
        soup = BeautifulSoup(page.content, "html.parser")
        img_link = soup.find("img", class_="dinosaur--image")["src"]

        d_name_description = soup.find_all("dl", class_="dinosaur--name-description")
        d_des = soup.find_all("dl", class_="dinosaur--description dinosaur--list")
        d_info = soup.find_all("dl", class_="dinosaur--info dinosaur--list")
        d_content = soup.find(class_="dinosaur--content-container small-12 medium-12 large-12 columns")
        d_namedby = soup.find("dt", string="Named by:").find_next("dd").string
        list1.append('Named by:')
        list2.append(d_namedby)
        d_species = d_namedby.find_next("dd").string
        list1.append('Species type:')
        list2.append(d_species)

        for d in d_name_description:

            dts = d.find_all("dt")
            dds = d.find_all("dd")
            for i in dts:
                list1.append(i.text)
            for i in dds:
                list2.append(i.text.strip())

        for d in d_des:

            dts = d.find_all("dt")
            dds = d.find_all("dd")
            for i in dts:
                list1.append(i.text)
            for i in dds:
                list2.append(i.text.strip())

        for d in d_info:

            dts = d.find_all("dt")
            dds = d.find_all("dd")
            for i in dts:
                list1.append(i.text)
            for i in dds:
                list2.append(i.text.strip())
        try:
            if (d_content.text):
                list1.append("content")
                list2.append(d_content.text)
        except Exception as e:
            print("entered Exception")
            print(e)
        info = zip(list1, list2)
        print(getsizeof(info))
    return render(request, 'app/index.html', {'info': info, 'dinos': dinos, 'img': img_link, 'name': name})

def randomdino(request):
    dino = random.choice(dinos)
    print(dino)
    name = dino
    list1 = []
    list2 = []
    page_link = "https://www.nhm.ac.uk/discover/dino-directory/" + name.lower() + ".html"

    page = requests.get(page_link)
    soup = BeautifulSoup(page.content, "html.parser")
    img_link = soup.find("img", class_="dinosaur--image")["src"]

    d_name_description = soup.find_all("dl", class_="dinosaur--name-description")
    d_des = soup.find_all("dl", class_="dinosaur--description dinosaur--list")
    d_info = soup.find_all("dl", class_="dinosaur--info dinosaur--list")
    d_content = soup.find(class_="dinosaur--content-container small-12 medium-12 large-12 columns")
    try:
        d_namedby = soup.find("dt", string="Named by:").find_next("dd").string
    except Exception as e:
        d_namedby = None
        print(e)

    list1.append('Named by:')
    list2.append(d_namedby)
    d_species = d_namedby.find_next("dd").string
    list1.append('Species type:')
    list2.append(d_species)

    for d in d_name_description:

        dts = d.find_all("dt")
        dds = d.find_all("dd")
        for i in dts:
            list1.append(i.text)
        for i in dds:
            list2.append(i.text.strip())

    for d in d_des:

        dts = d.find_all("dt")
        dds = d.find_all("dd")
        for i in dts:
            list1.append(i.text)
        for i in dds:
            list2.append(i.text.strip())

    for d in d_info:

        dts = d.find_all("dt")
        dds = d.find_all("dd")
        for i in dts:
            list1.append(i.text)
        for i in dds:
            list2.append(i.text.strip())
    try:
        if (d_content.text):
            list1.append("content")
            list2.append(d_content.text)
    except Exception as e:
        print("entered Exception")
        print(e)
    info = zip(list1, list2)
    return render(request, 'app/index.html', {'rinfo': info, 'dinos': dinos, 'img': img_link, 'name': name})

def herbivores(request):
    num = len(herbs)
    return render(request, 'app/category.html', {'dinos': herbs, 'title': 'Herbivores', 'num': num})
def carnivores(request):
    num = len(carns)
    return render(request, 'app/category.html', {'dinos': carns, 'title': 'Carnivores', 'num': num})
def omnivorous(request):
    num = len(omnis)
    return render(request, 'app/category.html', {'dinos': omnis, 'title': 'Omnivores', 'num': num})