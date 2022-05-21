from bs4 import BeautifulSoup
import requests

# add 2 numbers together and return the value only
import requests


def add_two_numbers(x, y):
    return (x+y)

# we need to print out our output
# print(add_two_numbers(3, 41))

# add 2 numbers and print the output
def add_two_numbers(x, y):
    print(x+y)
    return

# add_two_numbers(11, 11)

# function that uses requests and beautifulsoup to get the html data from a website
def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return r

print(get_soup('http://www.google.co.uk'))