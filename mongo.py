import random
from pymongo import MongoClient

#database
db = MongoClient().junhaojenny
#collection
accounts = db.accounts

def getAccounts():
    list = []
    results = accounts.find({})
    for dict in results:
        list.append(dict)
    return list

#list of dictionaries
accountList = getAccounts()


# returns a list of values matching the key
def getListOf(key):
    list = []
    results = accounts.find({})
    for dict in results:
        list.append(dict[key])
    return list


# `dict` arguments are assumed to have valid keys (e.g. 'user', 'password')

# what criteria for a valid password?
# subject to change
def isValidRegister(dict):
    newUser = dict['user']
    if newUser not in getListOf('user'):
        return True
    else:
        return False

def isValidLogin(dict):
    query = accounts.find(dict)
    if query.count() > 0:
        return True
    else:
        return False

def insert(dict):
    #db = MongoClient().junhaojenny
    #accounts = db.accounts
    accounts.insert(dict)
