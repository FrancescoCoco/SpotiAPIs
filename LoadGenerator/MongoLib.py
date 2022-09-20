"""
███╗░░░███╗░█████╗░███╗░░██╗░██████╗░░█████╗░██╗░░░░░██╗██████╗░
████╗░████║██╔══██╗████╗░██║██╔════╝░██╔══██╗██║░░░░░██║██╔══██╗
██╔████╔██║██║░░██║██╔██╗██║██║░░██╗░██║░░██║██║░░░░░██║██████╦╝
██║╚██╔╝██║██║░░██║██║╚████║██║░░╚██╗██║░░██║██║░░░░░██║██╔══██╗
██║░╚═╝░██║╚█████╔╝██║░╚███║╚██████╔╝╚█████╔╝███████╗██║██████╦╝
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░░╚════╝░╚══════╝╚═╝╚═════╝░
"""
import pymongo


def mongo_auth():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    dbmongo = myclient['Mongo_Metrics']
    return dbmongo


def add_item_to_collection(dbmongo, namecollection, item):
    mycol = dbmongo[namecollection]
    return mycol.insert_one(item)


def verify_collection(dbmongo, namecollection):
    if namecollection not in dbmongo.list_collection_names():
        return True


def get_items_from_collection(dbmongo, namecollection):
    mycol = dbmongo[namecollection]
    return mycol.find_one()
