import random

def primary():

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes[12])

if __name__== "__main__":
  primary()
