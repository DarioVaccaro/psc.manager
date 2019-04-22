import json
import csv
import os
from pymongo import MongoClient

def migration(source , map):
    migration = MIGRATE(source , map)
    manual = migration.manual()
    for row in migration.reader:
        migration_object = {}
        for key in manual.keys():
            migration_object[key] = manual[key]
        direct = migration.direct(row)
        for key in direct.keys():
            migration_object[key] = direct[key]
        unique = migration.unique(row)
        for key in unique.keys():
            migration_object[key] = unique[key]
        print(migration_object)

class MIGRATE(object):
    def __init__(self , source , map):
        self.source = open(source , 'r+')
        self.reader = csv.DictReader(self.source)
        with open(map , 'rb') as config:
            self.map = json.load(config)

    def manual(self):
        manual_input = {}
        for manual in self.map['manual'].keys():
            manual_input[manual] = input('Enter value for ' + str(manual) + ': ')

        return manual_input

    def direct(self , row):
        direct_values = {}
        for direct in self.map['direct'].keys():
            map_key = self.map['direct'][direct]
            if isinstance(map_key , dict):
                direct_values[direct] = {}
                for key in map_key:
                    direct_values[direct][key] = (row[map_key[key]] , '')[str(row[map_key[key]]) == '0']
            else:
                direct_values[direct] = (row[map_key] , '')[str(row[map_key]) == '0']

        return direct_values

    def unique(self , row):
        unique_values = {}
        for unique in self.map['unique'].keys():
            map_key = self.map['unique'][unique]
            unique_values[unique] = row[map_key]

        return unique_values

    def functions(self , row):
        print('Functions')

if __name__ == '__main__':
    customer_migration = migration('./bin/nameaddr.csv' , './migration/customers.json')