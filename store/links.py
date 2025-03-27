import pymongo
from store.manage_mongo import get_collection, remove_collection


DATABASE_NAME = 'utilities'
COLLECTION_NAME = 'links'

def add_links(author, link, description):
    coll = get_collection(DATABASE_NAME, COLLECTION_NAME)
    coll.insert_one({'author':author, 'link':link, 'description':description})
    print(f"added link {link} {description}")    

def get_links():
    coll = get_collection(DATABASE_NAME, COLLECTION_NAME)
    res = coll.find({})
    return [x for x in res]

if __name__=="__main__":
    add_links('test','www.google.com','search engine')
    for i in get_links():
        print(i)

    #remove_collection(DATABASE_NAME, COLLECTION_NAME)