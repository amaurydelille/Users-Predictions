import string
import random

def buildID():
    alphabet = []
    for letter in string.ascii_lowercase:
        alphabet.append(letter)
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    id = ""
    for k in range(6):
        id += numbers[random.randint(0, 8)]
        id += alphabet[random.randint(0, 24)]
    return id

def buildGender():
    gender = ["male", 'female', 'other']
    return gender[random.randint(0, 2)]


class Client:
    def __init__(self, id, age, gender, h_w, i_w):
        self.id = id
        self.age = age
        self.gender = gender
        self.h_w = h_w #hours/week, the time that an user spend per week on the app.
        self.i_w = i_w #number of interactions with the content per week (comments, likes, subscribes or shares).


def create_data_set(nb):
    """
    Create a set of clients.
    :param nb: number of clients models that we want to create.
    :return: a list of clients from the Cllient class.
    """
    clients = []
    for i in range(nb):
        temp = []
        id = buildID()
        age = random.randint(21, 60)
        gender = random.randint(0, 2)
        h_w = random.randint(1, 100)
        i_w = random.randint(1, 500)
        client = Client(id, age, gender, h_w, i_w)
        temp.append(client.id)
        temp.append(client.age)
        temp.append(client.gender)
        temp.append(client.h_w)
        temp.append(client.i_w)
        clients.append(temp)
    return clients

