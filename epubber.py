from renamer import *
from scraper import *
# from mover import *


"""
    after it has renamed, move to its correct folder
    command line
    scraping the website and downloading not working unless figure a way to login properly...
    automating the clicks might be a better option at this point(selenium?)
"""


def main():
    # login()
    renamer()
    print("Success!")


if __name__ == "__main__":
    main()
