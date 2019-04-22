import json
import csv
import os

class MIGRATE(object):
    def __init__(self , input):
        self.input = input

    def customers(self):
        print('Customers')

    def balls(self):
        print('Balls')

if __name__ == '__main__':
    print('Migration')

    # Add Migration key to customer schema
    # After balls migration, remove migration key