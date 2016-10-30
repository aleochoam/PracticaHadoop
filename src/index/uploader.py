from pymongo import MongoClient
import sys

def main():
    client = MongoClient()
    db = client.bigdata
    coll = db.indice

    file = open(sys.argv[1], 'r')
    for line in file:
        pair = line.split('\t', 1)
        result = coll.insert_one(
         {
            word: list(set(fileTimes))
         })

    file.close()


if __name__ == '__main__':
    main()