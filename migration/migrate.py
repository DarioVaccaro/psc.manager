import json
import csv
import glob
import os
from pymongo import MongoClient

# Import all python files in directory

def migration(source , map):
    client = MongoClient(os.environ["MONGODB_PS_URI"] , 
		connectTimeoutMS=30000,
		socketTimeoutMS=None)

    db = client.get_database()
    customers = db.customers
    
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
        functions = migration.functions(row)
        for key in functions.keys():
            migration_object[key] = functions[key]
        process = migration.process(row)
        for key in process.keys():
            migration_object[key] = process[key]
        
        print(migration_object)
        customers.insert_one(migration_object)

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
        functions_values = {}
        for functions in self.map['functions'].keys():
            map_key = self.map['functions'][functions]
            functions_values[functions] = getattr(__import__(map_key['package']) , map_key['function'])(map_key['param'])
        
        return functions_values

    def process(self , row):
        process_values = {}
        for process in self.map['process'].keys():
            map_key = self.map['process'][process]
            process_values[process] = ''
            for value in map_key['field']:
                process_values[process] += row[value] + map_key['separator']
            process_values[process] = process_values[process][:-(len(str(map_key['separator'])))]
        
        return process_values

if __name__ == '__main__':
    path = os.path.abspath(__file__)
    directory = os.path.dirname(path)
    os.chdir(directory)

    while True:
        source = input('Enter Path of Source CSV: ')
        map = input('Enter Path of Map JSON: ')

        customer_migration = migration(source , map)