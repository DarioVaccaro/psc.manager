from random import randint
from datetime import datetime

def generate_id(param):
    id = ''
    selection = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    for key in range(17):
        id += selection[randint(0 , len(selection) - 1)]

    return param + '_' + id

def generate_date(param):
    return int(datetime.now().timestamp() * 1000)