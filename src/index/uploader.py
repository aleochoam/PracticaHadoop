from pymongo import MongoClient
import sys

def main():
    client = MongoClient()
    db = client.bigdata
    coll = db.indice

    file = open(sys.argv[1], 'r')
    for line in file:
        pair = line.split('\t', 1)
        pair1 = pair[1].split(", ")
        for x in pair1:
            print(x + "ESTO")
        # result = coll.insert_one(
        #  {
        #     "Palabra" : pair[0],
        #     "docs" : [
        #         {
        #             "nombre":
        #         }
        #     ]
        #     pair[0]: pair[1]
        #  })

    file.close()


if __name__ == '__main__':
    main()