from bs4 import BeautifulSoup, Tag
import random

def shall_i_shuffle():
    choices = [0, 1]
    random_choice = random.choice(choices)
    if random_choice:
        return True
    return False

def shuffle(page):
    class_set = set()
    with open(page, 'r+') as fl:
        soup = BeautifulSoup(fl, 'html.parser')
    body = soup.find('body')
    for element in body.find_all(recursive=True):
        if isinstance(element, Tag):
            classes = element.get('class')
            if classes:
                for cls in classes:
                    class_set.add(cls)

    with open(page, 'r+') as fl:
        soup = BeautifulSoup(fl, 'html.parser')
    everything = soup.findAll(recursive=True)
    for element in everything:
        if isinstance(element, Tag):
            classes = element.get('class')
            if classes and shall_i_shuffle():
                class_length = len(classes)
                random_class = []
                for i in range(0, class_length):
                    random_class.append(random.choice(list(class_set)))
                element['class'] = random_class
    return soup