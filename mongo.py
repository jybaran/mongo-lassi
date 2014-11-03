#import random
from pymongo import MongoClient
import datetime

#database
db = MongoClient().junhaojenny

#collection
accounts = db.accounts

# `dict` arguments are assumed to have valid keys (e.g. 'user', 'password')

# what criteria for a valid password?
def isValidRegister(dict):
    newUser = dict['user']
    query = accounts.find({'user':newUser})
    if query.count() == 0:
        return True
    else:
        return False

def isValidLogin(dict):
    query = accounts.find(dict)
    if query.count() > 0:
        return True
    else:
        return False

def addAccount(dict):
    dict['date_created'] = datetime.date.today().strftime("%B %d, %Y")
    accounts.insert(dict)
