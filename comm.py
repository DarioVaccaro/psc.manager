import csv
import json
from collections import OrderedDict

def ex(data , filename):
    keys = []

    for collection in data:
        key_list = list(collection.keys())
        for key in key_list:
            if(key not in keys):
                keys.append(key)

    with open('bin/' + filename + '.csv' , 'w') as export:
        writer = csv.DictWriter(export , fieldnames = keys)
        writer.writeheader()
        writer.writerows(data)