import random


def primary():

    f = open("quotes.txt")
    quotes = f.readlines()
    quotes_quant = quotes.__len__()
    random_quote = quotes[random.randint(0, quotes_quant)]
    f.close()

    print(random_quote, end="")


if __name__ == "__main__":
    while True:
        user_input = input(
            "Press Enter for a new quote, or C and Enter to close")
        if user_input == "c":
            print("Goodbye", end="")
            break
        if user_input == "":
            primary()
