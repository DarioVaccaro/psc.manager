import csv
import json
from collections import OrderedDict

def im():
    print('Import')

def ex(data , filename):
    keys = []

    for collection in data:
        key_list = list(collection.keys())
        for key in key_list:
            if(key not in keys):
                keys.append(key)

    # Export to JSON and CSV
    with open('var/' + filename + '.csv' , 'w') as export:
        writer = csv.DictWriter(export , fieldnames = keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    print('IO')