import os

from collections import namedtuple

from .utils import Colors

def read_list():
    # path = raw_input('Enter path to BOM: ')
    path = '/Users/alexfeldman/Documents/Scripts/BOM/tester.txt'
    ext = os.path.splitext(path)[1]
    if ext == '.txt':
        with open(path, 'r') as text_file:
            lines = text_file.readlines()
        if len(lines):
            print Colors.success('Read successfuly')
    items = []
    Item = namedtuple('Item', 'reference, quantity, value')



if __name__ == '__main__':
    read_list()
