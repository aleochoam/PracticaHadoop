import sys

databaseName = "bigdata"
collectionName = "indice"


def initDB():
    client = MongoClient()
    db = client[databaseName]
    coll = db[collectionName]


def readfile(name):
    file = open(name, 'r')
    for line in file:
        pair = line.split('\t', 1)
        upload(pair)

def upload(pair):
    # print( "Subiendo {\n" + pair[0]+ " : " + pair[1] + "\n}")
    result = coll.insert_one(
         {
            word: list(set(fileTimes))
         })

def main():
    initDB()
    readfile(sys.argv[1])

if __name__ == '__main__':
    main()