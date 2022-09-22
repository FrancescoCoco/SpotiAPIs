"""
███╗░░░███╗░█████╗░███╗░░██╗░██████╗░░█████╗░██╗░░░░░██╗██████╗░
████╗░████║██╔══██╗████╗░██║██╔════╝░██╔══██╗██║░░░░░██║██╔══██╗
██╔████╔██║██║░░██║██╔██╗██║██║░░██╗░██║░░██║██║░░░░░██║██████╦╝
██║╚██╔╝██║██║░░██║██║╚████║██║░░╚██╗██║░░██║██║░░░░░██║██╔══██╗
██║░╚═╝░██║╚█████╔╝██║░╚███║╚██████╔╝╚█████╔╝███████╗██║██████╦╝
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░░╚════╝░╚══════╝╚═╝╚═════╝░
"""
from collections.abc import Mapping
from typing import Any

import pymongo
from pymongo.database import Database


def mongo_auth():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    dbmongo = myclient.get_database('Mongo_Metrics')
    return dbmongo


def add_item_to_collection(dbmongo: Database[Mapping[str, Any]], namecollection, item):
    mycol = dbmongo[namecollection]
    return mycol.insert_one(item)


def verify_collection(dbmongo, namecollection, cpu):
    if namecollection not in dbmongo.list_collection_names():
        return True
    results = list(dbmongo[namecollection].find(({
        "cpu": {"$eq": cpu}
    })))
    if len(results) == 0:
        return True
    else:
        return False


def get_items_from_collection(dbmongo: Database[Mapping[str, Any]], namecollection, cpu):
    return dbmongo.get_collection(namecollection).find({
        "cpu": {"$eq": cpu}
    })


def get_items_from_collection_by_numberartists(dbmongo: Database[Mapping[str, Any]], namecollection, cpu, number_artists):
    return dbmongo.get_collection(namecollection).find({
        "cpu": {"$eq": cpu},
        "number_artists":{"$eq": number_artists}
    })
