import os
import re
import sys
import unicodedata

from pymongo import MongoClient
from mrjob.job import MRJob


databaseName = "bigdata"
collectionName = "indice"

client = None
db     = None
coll   = None

timesMap = {}

def initDB():
    client = MongoClient()
    db = client[databaseName]
    coll = db[collectionName]


def limpiar(line):
    line = line.lower()
    line = elimina_tildes(line)
    line = re.findall(r"[\w']+", line)
    return line

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def getKey(item):
    return item[1]

def sortByTimes(oldList):
    return sorted(oldList,key=getKey, reverse=True)

class InvertedIndex(MRJob):

    def mapper(self, _, line):
        fileName = os.environ['map_input_file']
        line = limpiar(line)

        for word in line:
            if (fileName, word) not in timesMap:
                timesMap[(fileName, word)] = 1
            else:
                timesMap[(fileName, word)] +=1

            yield (word, fileName)

    def reducer(self, word, files):
        lFiles = list(files)
        fileTimes = [(x, timesMap[(x, word)]) for x in lFiles]

        newList = sortByTimes(list(set(fileTimes)))
        json = {
            "Palabra" : word,
            "docs" : []
        }
        for x in newList:
            json["docs"].append({"nombre" : x[0], "veces": x[1]})

        result = coll.insert_one(json);
        print ("Subio uno", file=sys.stderr)
        yield word, newList

if __name__ == '__main__':
    initDB()
    InvertedIndex.run()
