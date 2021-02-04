import random
import requests
import json

class Person(object):
    """person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

young = []
old = []
for pers in range(1, 10):
    response = requests.get('https://api.randomdatatools.ru/?count=1?params=FirstName')
    text = json.loads(response.text)
    name = text["FirstName"]
    pers = Person(name, random.randrange(100))
    if pers.age < 50:
        young.append(pers)
    else:
        old.append(pers)

print("Вывод списка молодых:")
for pers in young:
    print(pers.name, pers.age)
print("Вывод списка старых:")
for pers in old:
    print(pers.name, pers.age)
