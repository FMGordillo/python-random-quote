import random


def primary():

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes[random.randint(0, quotes.__len__() - 1)])


if __name__ == "__main__":
    primary()
