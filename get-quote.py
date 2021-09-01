import random

def primary():

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes[random])

if __name__== "__main__":
  primary()
